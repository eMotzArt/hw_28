Before launch for source-launch:
1) python -m venv venv
2) source venv/bin/activate
3) pip install poetry
4) poetry install 
5) python manage.py import_data
6) python manage.py runserver 0.0.0.0:8000

For docker-launch:
docker build -t SOME_NAME
docker run -d -p 80:8000 SOME_NAME