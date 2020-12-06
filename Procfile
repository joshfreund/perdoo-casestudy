web: gunicorn casestudy.wsgi --log-file -
worker: celery -A casestudy.celery worker -B --loglevel=info