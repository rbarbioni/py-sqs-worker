# gzapi
Standard sample GrupoZap project worker using tools and best practices for organization.


## Application Checklist

- [x] Python 3.6
- [x] Dynaconf
- [x] Localstack
- [x] Pipenv
- [x] Docker
- [x] Docker-Compose
- [x] Gelf Logger
- [x] Flake8
- [x] Sentry
- [x] Prometheus

#### Local
* just run the command
    ```bash
    make install
    make run/local

## How To Run
#### Docker-Compose
* just run the command
    ```bash
    make run/docker-compose
    ```

#### Docker Only
* just run the command
    ```bash
    make run/docker
    ```

#### Lint
* just run the command
    ```bash
    make lint
    ```

## Replace Project Name
* just run the command
    ```bash
    find /home/renan/dev/workspaces/temp/pygz-api -type f -exec sed -i "s/namespace/yournamespace/g; s/py-sqs-worker/yourprojectname/g" {} +
    ```
