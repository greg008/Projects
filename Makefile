.PHONY: test


deps:
	pip install -r requirements.txt
	pip install -r test_requirements.txt

lint:
	flake8 WhenShouldIBuy/

run:
	PYTHONPATH=./WhenShouldIBuy python ./WhenShouldIBuy/main.py

docker_build:
	docker build -t my_projects .

docker_run: docker_build
			docker run \
				--name my_projects_container \
				-d my_projects

USERNAME=greg008
TAG=$(USERNAME)/my_projects

docker_push: docker_build
				@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
				docker tag my_projects $(TAG); \
				docker push $(TAG); \
				docker logout;
