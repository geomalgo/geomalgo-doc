.PHONY: test checkdoc mypy


checkdoc:
	python checkdoc.py ../../geomalgo


test:
	PYTHONPATH=. nosetests --with-doctest


mypy:
	mypy checkdoc.py
