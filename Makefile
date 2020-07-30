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
				-dit my_projects
