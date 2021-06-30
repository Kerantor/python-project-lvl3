install:
	poetry install

test:
	poetry run pytest page_loader tests

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests

lint:
	poetry run flake8 page_loader

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

pageloader:
	poetry run page_loader -h

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

