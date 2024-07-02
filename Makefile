build:
	docker build -t plw-test .

test:
	docker run -it --rm --network=host plw-test
