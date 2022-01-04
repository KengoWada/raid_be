# RAiD Backend

## Getting Started

- Create a virtual environment `python3 -m venv venv`

- Activate the virtual environment `. venv/bin/activate`

- Install all dependencies `pip install -r requirements.txt`

- Create a `.env` file and add the variables from `.env_example`

- Source the environment variables `source .env`

- Make databse migrations `python manage.py migrate`

- Run the server `python manage.py runserver`

## Deploying To Compute Engine

- Clone the repo

- Install the needed dependencies `apt-get install redis-server postgresql nginx postgresql-contrib libpcap-dev libpq-dev`

- Configure PostgreSQL, Redis and Nginx accordingly

- Create a virtual environment `python3 -m venv venv`

- Activate the virtual environment `. venv/bin/activate`

- Install all dependencies `pip install -r requirements.txt`

- Create a `.env` file and add the variables from `.env_example`

- Make databse migrations `python manage.py migrate`

- Create `static` and `media` directories then run `python manage.py collectstatic`

- Start the server `gunicorn api.wsgi -b 0.0.0.0:8080 --timeout 900 --log-level debug --log-file -`
