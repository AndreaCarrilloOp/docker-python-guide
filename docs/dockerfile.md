# Dockerfile reference

[Course home](../README.md)

The four examples use the same container-building principles. Compare the actual [Flask Dockerfile](../modules/01-containerization/flask-basic/Dockerfile) and [FastAPI Dockerfile](../modules/01-containerization/fastapi-basic/Dockerfile).

| Instruction | Purpose |
| --- | --- |
| FROM | Use an official Python 3.11 slim image. |
| ENV | Disable bytecode files and enable unbuffered output. |
| WORKDIR | Set the application directory. |
| COPY requirements.txt / RUN pip | Install dependencies before copying code for layer caching. |
| COPY | Include the application source. |
| USER | Run the application without root privileges. |
| EXPOSE | Document the application port; publish it using `-p`. |
| HEALTHCHECK | Probe the local HTTP health endpoint. |
| CMD | Define the default application command. |

## Build and inspect

From an example directory:

```bash
docker build -t guide-example .
docker image ls guide-example
docker history guide-example
```

Use `.dockerignore` to exclude caches, local environments and sensitive files. Copy frequently changed source after dependencies. The application runs as a non-root user; installing dependencies at build time does not require the runtime user to be root. Avoid storing passwords in Dockerfiles or images.

Optional templates: [basic](../modules/01-containerization/templates/Dockerfile.basic) and [multi-stage](../modules/01-containerization/templates/Dockerfile.multistage). They are reference templates, not additional required modules.

See [security notes](security.md) for credential handling.
