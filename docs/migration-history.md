# Migration history

The original tutorial consisted of six branches. The consolidated layout keeps the five learning checkpoints in one tree. Earlier implementations are retained at these immutable commits (legacy setup commands are not required for the new guide).

| Original module | Source commit |
|---|---|
| Containerization | [90bf947](https://github.com/AndreaCarrilloOp/docker-python-guide/tree/90bf947abce8d0ebd669092d93e777c377e39ed1) |
| Development | [fcf547e](https://github.com/AndreaCarrilloOp/docker-python-guide/tree/fcf547efed8ae65f1c40a7fb0d585786b247b67f) |
| Linting and typing | [930ad39](https://github.com/AndreaCarrilloOp/docker-python-guide/tree/930ad397f05f114ef8f1e3f77cd3be1d86ceb7dc) |
| CI/CD | [db1666c](https://github.com/AndreaCarrilloOp/docker-python-guide/tree/db1666c4354640f764a57d3db766e6929a0904f8) |
| Deployment | [cb76adc](https://github.com/AndreaCarrilloOp/docker-python-guide/tree/cb76adc7c6aa9e5bdfee532c98f559af6594e5fe) |

The new Flask task and FastAPI Redis paths deliberately carry the same APIs forward from development through deployment. Legacy deployment-only examples, branch setup scripts and duplicate configurations remain in the original commits, not in the active tutorial. The new layout does not automatically erase old credential material from Git history. Rotate any credentials that were ever real, and review repository history before deleting or archiving the old branches.
