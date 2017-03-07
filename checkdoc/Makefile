.PHONY: test checkdoc mypy

checkdoc:
	python checkdoc.py ../../geomalgo

test:
	PYTHONPATH=. python test/test_checkdoc.py

mypy:
	mypy checkdoc.py
