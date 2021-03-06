cleanfiles:
	find . -name \*.pyc -delete
	find . -name \*__pycache__ -delete
	find . -name \*~ -delete

install:
	pipenv install --dev

shell:
	pipenv shell

lint:
	flake8 __main__.py app/*

lint/fix:
	autopep8 --global-config .flake8 --in-place --aggressive --recursive .

test:
	python -m pytest --cov=app ./tests -vv

run:
	python main.py

run/docker:
	docker build -t rbarbioni/py-sqs-worker:latest . \
	&& docker run -it \
	-e AWS_ACCESS_KEY_ID=foo \
	-e AWS_SECRET_ACCESS_KEY=foo \
	-e AWS_DEFAULT_REGION=us-east-1 \
	--net=host \
	rbarbioni/py-sqs-worker:latest

run/docker-compose:
	docker-compose -f docker-compose.yml up --build

run/docker-compose-structure:
	docker-compose -f docker-compose.yml up --scale py-sqs-worker=0 -d

build/docker:
	docker-compose build --force-rm py-sqs-worker

send-message:
	python sender.py

