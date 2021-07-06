all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && venv/bin/pip install ../hseling_lib_poem_generator && venv/bin/pip install .

run: venv
	FLASK_APP=hseling_api_poem_generator venv/bin/flask run

test: venv
	HSELING_API_POEM_GENERATOR_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist: venv test
	venv/bin/python setup.py sdist
