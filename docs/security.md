# Security notes

- Use a fresh random password for each local PostgreSQL lab. Copy `.env.example` to `.env`; set POSTGRES_PASSWORD before starting Compose.
- Bind example HTTP ports to loopback; PostgreSQL and Redis remain on the private service network.
- Docker images run application processes as non-root users. Health checks use Python's standard library.
- Module 05 does not store a Secret manifest with credential values. Create the Secret interactively in your own local cluster.
- The original deployment branch contains a password file and a Secret manifest; the migration does not copy them. Their previous versions remain in Git history. If any historical credentials were real, revoke or rotate them. Removing files or branches does not guarantee removal from clones or GitHub caches.
- This review covers known sensitive paths and active tutorial configuration; it is not a full historical secret scan or dependency vulnerability audit.
- APIs intentionally lack authentication for local training. Do not expose them to the Internet.
