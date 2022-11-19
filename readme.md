Source-launch:
1) python3 -m venv venv
2) source venv/bin/activate
3) pip install poetry
4) poetry install 
5) run postgres (in terminal: docker run --name hw28 -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres)
6) python3 manage.py migrate
7) python3 manage.py import_data
8) python3 manage.py runserver localhost:8000



For docker-launch:
docker build -t SOME_NAME .

docker run -d -p 80:8000 SOME_NAME
