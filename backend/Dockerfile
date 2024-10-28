FROM python:3.13.0-slim
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

COPY ./entrypoint.sh . 
ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]