python3 manage.py migrate
python3 manage.py collectstatic

gunicorn --bind 0.0.0.0:8000 --workers 3 resume_api.wsgi:application