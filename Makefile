.PHONY: test
test: export PYTHONPATH = example
test:
	python -B -m unittest -v -b
