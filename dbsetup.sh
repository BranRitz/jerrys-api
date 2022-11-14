#docker-compose run api python manage.py migrate survey_api zero
docker-compose run api python manage.py makemigrations
docker-compose run api python manage.py migrate
docker-compose run api python manage.py shell < ./populate_db.py