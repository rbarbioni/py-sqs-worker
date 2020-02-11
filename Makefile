cleanfiles:
	find . -name \*.pyc -delete
	find . -name \*__pycache__ -delete
	find . -name \*~ -delete

install:
	pipenv install --dev

lint:
	flake8 __main__.py app/*

lint/fix:
	autopep8 --global-config .flake8 --in-place --aggressive --recursive .

test:
	python -m pytest --cov=app ./tests -vv

run:
	python main.py

run/docker:
	docker build -t vivareal/gzworker:latest . \
	&& docker run -it \
	-e AWS_ACCESS_KEY_ID=foo \
	-e AWS_SECRET_ACCESS_KEY=foo \
	-e AWS_DEFAULT_REGION=us-east-1 \
	--net=host \
	vivareal/gzworker:latest

run/docker-compose:
	docker-compose -f docker-compose.yml up --build

run/docker-compose-structure:
	docker-compose -f docker-compose.yml up --scale gzworker=0 -d

build/docker:
	docker-compose build --force-rm gzworker

generate-deployment:
	cat deploy/deployment.template.yml | \
	sed "s/__TAG__/$(TAG)/g; \
	s/__IAM__/$(IAM)/g; \
	s/__REPLICAS__/$(REPLICAS)/g; \
	s/__REQUESTS.CPU__/$(REQUESTS_CPU)/g; \
	s/__REQUESTS.MEM__/$(REQUESTS_MEM)/g; \
	s/__LIMITS.CPU__/$(LIMITS_CPU)/g; \
	s/__LIMITS.MEM__/$(LIMITS_MEM)/g" > deploy/deployment.yml
deploy-kube: kubectl
	./kubectl apply --record -f deploy/secrets.yml --namespace=namespace
	./kubectl apply --record -f deploy/deployment.yml --namespace=namespace
	./kubectl apply --record -f deploy/service.yml --namespace=namespace
	./kubectl apply --record -f deploy/hpa.yml --namespace=namespace
	./kubectl apply --record -f deploy/$(DEPLOY_ENV)/ingress.yml --namespace=namespace

kubeconfig: kubectl
	./kubectl config set-cluster $(CLUSTER_NAME) --server="$(CLUSTER_ENDPOINT)" --insecure-skip-tls-verify
	./kubectl config set-credentials $(CLUSTER_NAME) --token="$(CLUSTER_TOKEN)"
	./kubectl config set-context $(CLUSTER_NAME) --cluster=$(CLUSTER_NAME) --user=$(CLUSTER_NAME) --namespace=namespace
	./kubectl config use-context $(CLUSTER_NAME)
kubectl:
	wget -O ./kubectl https://storage.googleapis.com/kubernetes-release/release/v1.13.10/bin/$(KERNEL)/amd64/kubectl
	chmod +x kubectl
notify-slack:
	curl -X POST -H 'Content-type:application/json' --data '{"text":"$(text)"}' $(SLACK_HOOK)