FROM python:3.9-slim

RUN apt-get update -y && apt-get install -y --no-install-recommends python3-dev gcc software-properties-common && \
  apt-get clean && \
  apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
  rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV FLASK_ENV=development
ENV FLASK_APP=app/app.py

CMD python manage.py