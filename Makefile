.PHONY: test


deps:
	pip install -r requirements.txt
	pip install -r test_requirements.txt

lint:
	flake8 WhenShouldIBuy/

run:
	PYTHONPATH=./WhenShouldIBuy python ./WhenShouldIBuy/main.py
