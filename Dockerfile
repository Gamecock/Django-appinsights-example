FROM  python:3.8.7-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY requirements.txt /src

RUN pip install -r requirements.txt

COPY . /src

CMD python manage.py runserver 0:8000