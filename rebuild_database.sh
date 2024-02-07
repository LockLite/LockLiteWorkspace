rm -rf LockLite/app/migrations
docker exec locklite-postgresql psql -U locklite -d locklite -c "DELETE FROM django_migrations WHERE app = 'app'"
python LockLite/manage.py makemigrations app
python LockLite/manage.py migrate
python LockLite/manage.py loaddata initial_data.json
