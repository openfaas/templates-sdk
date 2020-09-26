

lint:
	@echo "+ lint"
	@poetry run pylint function_sdk tests

fmt:
	@echo "+ fmt"
	@poetry run black .

test:
	@echo "+ build"
	@poetry run pytest .

build: lint fmt test
	@echo "+ build package"
	@poetry build
