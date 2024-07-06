lint:
	python -m flake8

# Docker
build:
	docker build -t plw-test .

test:
	docker run -it --rm --network=host plw-test
