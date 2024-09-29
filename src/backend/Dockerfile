FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app/app

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["fastapi", "run", "--host", "0.0.0.0"]

