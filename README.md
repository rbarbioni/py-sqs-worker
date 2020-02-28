# PySqsWorker
Python sample worker project that use SQS consumer messages and processing.

## Application Checklist

- [x] Python 3.6
- [x] Tests
- [x] Dynaconf
- [x] Localstack
- [x] Pipenv
- [x] Docker
- [x] Docker Swarm
- [x] Docker-Compose
- [x] Gelf Logger
- [x] Sentry
- [x] Flake8
- [x] Sentry
- [x] Prometheus

## Pyenv and Pipenv
To run this project locally, you need to install pyenv and pipenv in order to create the Python virtual environments
This project use Python 3.6

#### Pyenv
[Install Pyenv](https://github.com/pyenv/pyenv)

#### Pipenv
[Install Pipenv](https://github.com/pypa/pipenv)

## Before Run
If you don't have python 3.6 installed, run
```bash
pyenv install 3.6.9
```

Pipenv will use python 3.6.9 just instaled
```bash
make install
```

To activate this project's virtualenv, run pipenv shell.
```bash
make shell
```

## How To Run
#### Docker-Compose
Just run the command
```bash
make run/docker-compose
```

#### Docker-Compose Only Structure (localstack)
Just run the command
```bash
make run/docker-compose-structure
```

#### Local
Before, check if localstack is running correctly
```bash
docker ps
```

Just run the command
```bash
make run/local
```

#### Docker Only
Before, check if localstack is running correctly
```bash
docker ps
```

Just run the command
```bash
make run/docker
```

#### Lint
Just run the command
```bash
make lint
```

#### Tests
Just run the command
```bash
make test
```

## Send SQS Messages
The project have a sender.py function that sends message to localstack/AWS SQS and help in testing.
Before, check if application and localstack is running correctly!
```bash
make send
```
# Optional Arguments
- MESSAGES_COUNT: integer
- PAYLOAD: string

## Docker Swarm
To learn more about Docker Swarm, visit https://prometheus.io
This project is configured to run with docker swarm. [First configure docker swarm](https://www.dataquest.io/blog/install-and-configure-docker-swarm-on-ubuntu)
Create Docker Swarm node
```bash
docker swarm init --advertise-addr [your-localhost-ip-v4]
```

Create and initialize stack
```bash
docker stack deploy --compose-file="docker-compose.yml" py-sqs-worker
```

Docker Swarm configuration is defined in `deploy` configuration in docker-compose.yml file

## Replace Project Name
Just run the command
```bash
find . -type f -exec sed -i "s/py-sqs-worker/yourprojectname/g" {} +
```

## Prometheus Metrics
To learn more about Prometheus, visit https://prometheus.io
To access local metrics, access:
http://localhost:5000/metrics
Or
http://your-ipv4-ip:5000/metrics


## Sentry
To learn more about Sentry, visit https://sentry.io
Create a free Sentry account
Passing as application arguments the Sentry DSN
```bash
export SENTRY_DSN=YOUR-SENTRY-DSN
```

## Contributors
Just don't commit directly on master, push a branch and Pull Request.
