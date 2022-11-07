

FROM debian:bullseye-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essentail \
    gcc \
    libffi-dev \
    muls-dev \
    openssl \
    postgressql \
    libpq-dev

COPY requirements/prod.txt ./requirements/prod.txt
#RUN pip install -r requirements

COPY manage.py ./manage.py
COPY car_website ./car_website

EXPOSE 8000

FROM production as development

COPY requirements/dev.txt ./requirements/dev.txt
#RUN pip install -r ./requirements/dev.txt

COPY . .

