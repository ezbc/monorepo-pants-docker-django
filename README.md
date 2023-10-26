# Monorepo Pants Docker Django Poetry Example

## Setup

1. Export a virtual environment

   ```bash
   pants export --resolve=python-default
   ```
   
2. Package targets

   ```bash
   pants package ::
   ```
   
   A pex folder should be created at `dist/django_project/manage_local.pex`.

3. Run the docker containers with docker compose

   ```bash
   docker compose up web_server 
   ```

## Adding packages

Make your change to the poetry requirements in pyproject.toml then run 

```bash
pants generate-lockfiles
```
