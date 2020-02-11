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
- [x] Flake8
- [x] Sentry
- [x] Prometheus

## Pyenv and Pipenv
* To run this project locally, you need to install pyenv and pipenv in order to create the Python virtual environments
* This project use Python 3.6

#### Pyenv
* [Install Pynv](https://github.com/pyenv/pyenv)

#### Pipenv
* [Install Pipenv](https://github.com/pypa/pipenv)

## Before Run
* just run the command
    ```bash
    make install
    make shell

## How To Run
#### Docker-Compose
* just run the command
    ```bash
    make run/docker-compose
    ```

#### Docker-Compose Only Structure (localstack)
* just run the command
    ```bash
    make run/docker-compose-structure
    ```

#### Local
* before, check if localstack is running correctly
    ```bash
    docker ps
    ```
* just run the command
    ```bash
    make run/local
    ```

#### Docker Only
* before, check if localstack is running correctly
    ```bash
    docker ps
    ```
* just run the command
    ```bash
    make run/docker
    ```

#### Lint
* just run the command
    ```bash
    make lint
    ```

#### Tests
* just run the command
    ```bash
    make test
    ```

## Send SQS Messages
* The project have a sender.py function that sends message to localstack/AWS SQS and help in testing.
* Before, check if application and localstack is running correctly!
    ```bash
    make send
    ```
* Optional Arguments
- MESSAGES_COUNT: integer
- PAYLOAD: string

## Docker Swarm
* This project is configured to run with docker swarm. [First configure docker swarm](https://www.dataquest.io/blog/install-and-configure-docker-swarm-on-ubuntu)
* Create Docker Swarm node
    ```bash
    docker swarm init --advertise-addr [localhost-ip-v4]
    ```
* Create and initialize stack
    ```bash
    docker stack deploy --compose-file="docker-compose.yml" py-sqs-worker
    ```
* Docker Swarm configuration is defined in `deploy` configuration in docker-compose.yml file

## Replace Project Name
* just run the command
    ```bash
    find . -type f -exec sed -i "s/py-sqs-worker/yourprojectname/g" {} +
    ```
