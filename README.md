# Django-on-GCP
An example of running a Django project on GCP

## Build the container
docker-compose build 

## to run migrations for DB
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"

## To work in interactive shell
docker-compose run --rm app sh -c "python manage.py shell"

## To run development server 
docker-compose up
go to http://127.0.0.1:8000/

## To deploy to GCP
docker-compose run --rm app sh -c "python manage.py collectstatic" 

docker-compose -f docker-compose-deploy.yml run --rm --remove-orphans gcloud gcloud app deploy --project atlas-demo-459504

