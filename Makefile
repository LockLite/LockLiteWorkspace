MANAGEPY := LockLite/manage.py
DOCKER_NAME := locklite-postgresql

install:
	pip install -r requirements.txt
	docker compose up -d

start:
	docker start $(DOCKER_NAME)

shell:
	python $(MANAGEPY) shell

migrate:
	python $(MANAGEPY) makemigrations app
	python $(MANAGEPY) migrate

data:
	python $(MANAGEPY) loaddata initial_data.json

db:
	@echo "Launch Postgresql: psql postgres "
	@echo "List databases: \l or \list"
	@echo "Connect to a database: \c 'database name'"
	@echo "List the tables in a database: \dt"
	@echo "Exit Postgresql: \q"
	@echo "-----------------------------------------------------"
	docker exec -it $(DOCKER_NAME) psql -U locklite -d locklite

run:
	python $(MANAGEPY) runserver

stop:
	docker stop $(DOCKER_NAME)

requirements:
	pip freeze > requirements.txt

.PHONY: install start shell migrate data db run stop requirements
