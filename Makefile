build:
	sam build

deploy: build
	sam deploy

lint:
	sam validate
	pylint clear_lambda_storage.py handler.py

clean:
	rm -rf .aws-sam

.PHONY: build deploy lint clean

