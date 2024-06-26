<img src="LockLite/app/public/img/locklite.png" alt="Locklite" style="width: 500px;">

## About the project

A password manager.

## Built with

[![Django][Django.py]][Django-url]

## Installation

1. Install dependencies
    ```sh
    pip install -r requirements.txt
   ```
2. Create Docker container
    ```sh
    docker compose up -d
   ```
3. Seed database
    ```sh
    python manage.py loaddata initial_data.json
   ```


## Usage

- Start Docker
    ```sh
    docker start locklite-postgresql
   ```
- Run server
    ```sh
    python manage.py runserver
    ```
- Stop Docker
    ```sh
    docker stop locklite-postgresql
   ```
   
## Database
1. Make Migrations
    ```sh
    python manage.py makemigrations
   ```
   ```sh
    python manage.py migrate
   ```
2. Access database
    ```sh
    docker exec -it locklite-postgresql psql -U locklite -d locklite
     ```
3. Postgresql commands
    ```
    Launch Postgresql: psql postgres 
    List tables: \l or \list
    Connect to a database: \c 'database name'
    List the tables in a database: \dt
    Exit Postgresql: \q
     ```

<!-- MARKDOWN LINKS & IMAGES -->

[Django.py]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
