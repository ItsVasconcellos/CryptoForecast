FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN python -m venv venv

RUN ./venv/bin/pip install --no-cache-dir --upgrade pip

RUN ./venv/bin/pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /backend/app

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["fastapi", "run", "--host", "0.0.0.0"]

