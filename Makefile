dev-install:
	pip install -r requirements.txt dev-requirements.txt
install-build-deps:
	pip install pip-tools
install:
	pip install -r requirements.txt
pin:
	pip-compile --generate-hashes
	pip-compile dev-requirements.in --generate-hashes
runserver:
	docker compose up
test:
	docker compose run api pytest -v
