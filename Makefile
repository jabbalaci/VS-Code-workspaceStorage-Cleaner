list:
	cat Makefile

mypy:
	mypy --config-file mypy.ini *.py
