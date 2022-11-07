FROM python:3.9-slim
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt
COPY . /usr/src/app
EXPOSE 8000
CMD ["/bin/bash", "-c", "python manage.py import_data;python manage.py runserver 0.0.0.0:8000"]
