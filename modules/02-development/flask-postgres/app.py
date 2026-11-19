"""Containerized task API backed by PostgreSQL."""

import os
from datetime import UTC, datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import URL, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Task(db.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(100))
    description: Mapped[str] = mapped_column(default="")
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))

    def __init__(self, title: str, description: str = "") -> None:
        self.title = title
        self.description = description

    def to_dict(self) -> dict[str, int | str | bool]:
        return {"id": self.id, "title": self.title, "description": self.description,
                "completed": self.completed, "created_at": self.created_at.isoformat()}


def create_app(database_uri: str | None = None) -> Flask:
    app = Flask(__name__)
    uri: str | URL
    if database_uri is not None:
        uri = database_uri
    elif os.getenv("DATABASE_URL"):
        uri = os.environ["DATABASE_URL"]
    else:
        uri = URL.create("postgresql+psycopg2", username=os.environ["POSTGRES_USER"],
                         password=os.environ["POSTGRES_PASSWORD"], host=os.environ["DB_HOST"],
                         database=os.environ["POSTGRES_DB"])
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    db.init_app(app)

    @app.get("/")
    def home():
        return jsonify(message="Flask + PostgreSQL Example", environment=os.getenv("ENVIRONMENT", "development"))

    @app.get("/health")
    def health():
        try:
            db.session.execute(text("SELECT 1"))
        except SQLAlchemyError:
            db.session.rollback()
            return jsonify(status="unhealthy"), 503
        return jsonify(status="healthy")

    @app.get("/tasks")
    def get_tasks():
        return jsonify([task.to_dict() for task in db.session.scalars(db.select(Task)).all()])

    @app.get("/tasks/<int:task_id>")
    def get_task(task_id: int):
        return jsonify(db.get_or_404(Task, task_id).to_dict())

    @app.post("/tasks")
    def create_task():
        data = request.get_json(silent=True)
        if not isinstance(data, dict) or not isinstance(data.get("title"), str) or not data["title"].strip() or len(data["title"]) > 100:
            return jsonify(error="Title is required (1–100 characters)"), 400
        description = data.get("description", "")
        if not isinstance(description, str):
            return jsonify(error="Description must be text"), 400
        task = Task(title=data["title"].strip(), description=description)
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict()), 201

    @app.put("/tasks/<int:task_id>")
    def update_task(task_id: int):
        task = db.get_or_404(Task, task_id)
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify(error="JSON object required"), 400
        if "title" in data and (not isinstance(data["title"], str) or not data["title"].strip() or len(data["title"]) > 100):
            return jsonify(error="Invalid title"), 400
        if "description" in data and not isinstance(data["description"], str):
            return jsonify(error="Invalid description"), 400
        if "completed" in data and not isinstance(data["completed"], bool):
            return jsonify(error="Completed must be boolean"), 400
        for field in ("title", "description", "completed"):
            if field in data:
                setattr(task, field, data[field])
        db.session.commit()
        return jsonify(task.to_dict())

    @app.delete("/tasks/<int:task_id>")
    def delete_task(task_id: int):
        task = db.get_or_404(Task, task_id)
        db.session.delete(task)
        db.session.commit()
        return "", 204

    with app.app_context():
        db.create_all()
    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=os.getenv("FLASK_DEBUG") == "1")
