FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD echo "Hello my projects"
