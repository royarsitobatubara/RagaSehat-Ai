server-init:
	python -m venv .venv
	./.venv/Scripts/python.exe -m pip install -r requirements.txt
	mkdir -p model data

upgrade:
	pip freeze > requirements.txt

run-server: