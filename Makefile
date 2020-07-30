SERVICE_NAME=my_projects_container
MY_DOCKER_NAME=$(SERVICE_NAME)
.PHONY: test


deps:
	pip install -r requirements.txt
	pip install -r test_requirements.txt

lint:
	flake8 WhenShouldIBuy/

run:
	PYTHONPATH=./WhenShouldIBuy python ./WhenShouldIBuy/main.py

docker_build:
	docker build -t $(MY_DOCKER_NAME) .

docker_run: docker_build
			docker run \
				--name $(SERVICE_NAME) \
				-d $(MY_DOCKER_NAME)

USERNAME=greg008
TAG=$(USERNAME)/$(MY_DOCKER_NAME)

docker_push: docker_build
				@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
				docker tag $(MY_DOCKER_NAME) $(TAG); \
				docker push $(TAG); \
				docker logout;
