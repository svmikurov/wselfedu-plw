lint:
	python -m flake8

# Docker
build:
	docker build -t plw-test .

run:
	docker run -it --rm --network=host plw-test

test: build run
