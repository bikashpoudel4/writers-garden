build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d 

down:
	docker compose -f local.yml down

show-logs:
	docker compose -f local.yml logs

show-logs-api:
	docker compose -f local.yml logs api

makemigrations:
	docker compose -f local.yml run --rm api python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm api python manage.py migrate

collectstatic:
	docker compose -f local.yml run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm api python manage.py createsuperuser

down-v:
	docker compose -f local.yml down -v

volume:
	docker volume inspect src_local_postgres_data

postgres-backup:
	docker compose -f local.yml exec postgres backup

postgres-backups:
	docker compose -f local.yml exec postgres backups

writers-db:
	docker compose -f local.yml exec postgres psql --username=bikash --dbname=writers-heaven

flake8:
	docker compose -f local.yml exec api flake8 .

black-check:
	docker compose -f local.yml exec api black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec api black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec api black --diff --exclude=migrations .

isort-check:
	docker compose -f local.yml exec api isort . --check-only --skip venv --skip migrations

isort-diff:
	docker compose -f local.yml exec api isort . --diff --skip venv --skip migrations

isort:
	docker compose -f local.yml exec api isort . --skip venv --skip migrations

container-status:
	docker ps -a

clearcache:
	docker compose -f local.yml run --rm api python manage.py clearcache

dbshell:
	docker compose -f local.yml run --rm api python manage.py dbshell

search:
	docker compose -f local.yml exec api python manage.py search_index --create

search-rebuild:
	docker compose -f local.yml exec api python manage.py search_index --rebuild

search-populate:
	docker compose -f local.yml exec api python manage.py search_index --populate

test-coverage:
	docker compose -f local.yml run --rm api pytest -p no:warnings --cov=. -v

test-coverage-html:
	docker compose -f local.yml run --rm api pytest -p no:warnings --cov=. --cov-report html

pytest:
	docker compose -f local.yml run --rm api pytest