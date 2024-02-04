# writers-garden
## Advance Django application 

### Technologies used in this project 
  -   Use Docker with Celery, Redis, Elastic Search and Flower with Django REST Framework
  -   API testing with Pytest using factories and fixtures
  -   Shell scripts to automate and monitor processes
  -   Asynchronous tasks with Celery and Redis
  -   Asynchronous tasks monitoring with Flower
  -   Postgres within a Docker container, including how to perform backups using shell scripts.
  -   makefiles to make working with Docker
  -   Python Test coverage using coverage
  -   Logging in Django
  -   Token Based Authentication
  -   Emails using Mailhog in development

### To run an application
1. Start Docker Desktop
2. Open terminal
    - cd core
    - #### BUILD:
         -  docker compose -f local.yml up --build -d --remove-orphans
         -  make build
     - ### Make Migrations
         - docker compose -f local.yml run --rm api python manage.py makemigrations
         - make makemigrations
    - ### Migrate
        - docker compose -f local.yml run --rm api python manage.py migrate
        - make migrate

3. For more commands follow a file called Makefile in the core directory where all the commands are listed, the commands can be used as makefile and also can be used as normal

## Some of the important URLs in the app
- ### AdminPannel: http://localhost:8080/supersecret/
- ### Documentation: http://localhost:8080/redoc/
- ### Mailhog: http://localhost:8025/
- ### Elasticsearch: http://localhost:9200/
- ### Flower: http://localhost:5555/
- ### Nginx: http://localhost:8080/
