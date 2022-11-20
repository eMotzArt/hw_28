FROM python:3.9-slim
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt
COPY . /usr/src/app
#EXPOSE 8000
#CMD ["/bin/bash", "-c", "python manage.py migrate;python manage.py import_data;python manage.py runserver 0.0.0.0:8000"]
