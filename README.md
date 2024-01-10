<img src="LockLite/app/public/img/locklite.png" alt="Locklite" style="width: 500px;">

### About the project

A password manager.

### Built with

[![Django][Django.py]][Django-url]

### Usage

1. Install dependencies
    ```sh
    pip install -r requirements.txt
   ```
2. Seed database
    ```sh
    python manage.py loaddata initial_data.json
   ```
3. Migrations
    ```sh
    python manage.py makemigrations
   ```
   ```sh
    python manage.py migrate
   ```
4. Compose Docker
    ```sh
    docker compose up -d
   ```
5. Start Docker
    ```sh
    docker start locklite-postgresql
   ```
6. Access database
    ```sh
    docker exec -it locklite-postgresql psql -U locklite -d locklite
     ```
7. Run server
    ```sh
    python manage.py runserver
    ```
8. Stop Docker
    ```sh
    docker stop locklite-postgresql
   ```
9. Postgresql commands
	```sh
	Launch Postgresql: psql postgres 
	List tables: \l or \list
	Connect to a database: \c 'database name'
	List the tables in a database: \dt
	Exit Postgresql: \q
 	```

<!-- MARKDOWN LINKS & IMAGES -->

[Django.py]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
