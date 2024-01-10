install:
	pip install -r requirements.txt
	docker compose up -d

start:
	docker start locklite-postgresql

data:
	python LockLite/manage.py loaddata initial_data.json

migrate:
	python LockLite/manage.py makemigrations
	python LockLite/manage.py migrate

db:
	@echo "Launch Postgresql: psql postgres "
	@echo "List tables: \l or \list"
	@echo "Connect to a database: \c 'database name'"
	@echo "List the tables in a database: \dt"
	@echo "Exit Postgresql: \q"
	@echo "-----------------------------------------------------"
	docker exec -it locklite-postgresql psql -U locklite -d locklite

run:
	python LockLite/manage.py runserver

stop:
	docker stop locklite-postgresql

requirements:
	pip freeze > requirements.txt

.PHONY: install start data migrate db run stop requirements
