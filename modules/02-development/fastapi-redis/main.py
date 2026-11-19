"""Redis-backed API. Blocking Redis calls run in FastAPI's worker threads."""

import os
from datetime import UTC, datetime

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field
from redis import Redis
from redis.exceptions import RedisError

app = FastAPI(title="FastAPI + Redis Example")
cache = Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True,
                       socket_connect_timeout=3, socket_timeout=3)


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=3, max_length=254)


class User(UserCreate):
    id: int
    created_at: str


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "FastAPI + Redis Example", "docs": "/docs"}


@app.get("/health")
def health() -> dict[str, str]:
    try:
        cache.ping()
    except RedisError as error:
        raise HTTPException(503, "Redis unavailable") from error
    return {"status": "healthy"}


@app.get("/users", response_model=list[User])
def get_users() -> list[User]:
    users = []
    for key in cache.scan_iter("user:*"):
        data = cache.get(key)
        if isinstance(data, str):
            users.append(User.model_validate_json(data))
    return users


@app.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreate) -> User:
    user_id = cache.incr("user_counter")
    if not isinstance(user_id, int):
        raise HTTPException(503, "Unexpected Redis response")
    result = User(
        id=user_id, name=user.name, email=user.email,
        created_at=datetime.now(UTC).isoformat(),
    )
    cache.set(f"user:{result.id}", result.model_dump_json(), ex=3600)
    return result


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int) -> User:
    data = cache.get(f"user:{user_id}")
    if data is None:
        raise HTTPException(404, "User not found")
    if not isinstance(data, str):
        raise HTTPException(503, "Unexpected Redis response")
    return User.model_validate_json(data)


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int) -> Response:
    removed = cache.delete(f"user:{user_id}")
    if not isinstance(removed, int):
        raise HTTPException(503, "Unexpected Redis response")
    if removed == 0:
        raise HTTPException(404, "User not found")
    return Response(status_code=204)


@app.get("/cache/stats")
def get_cache_stats() -> dict[str, int]:
    count = cache.dbsize()
    if not isinstance(count, int):
        raise HTTPException(503, "Unexpected Redis response")
    return {"total_keys": count}


@app.delete("/cache/flush")
def flush_cache() -> dict[str, str]:
    if os.getenv("ENVIRONMENT") != "development":
        raise HTTPException(403, "Only available in development")
    # Delete only this tutorial's records, never unrelated Redis keys.
    for key in cache.scan_iter("user:*"):
        cache.delete(key)
    return {"message": "Tutorial records cleared"}
