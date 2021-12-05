FROM python:3.9.8 as base
FROM base as builder

WORKDIR /app

RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry lock && poetry export -f requirements.txt --without-hashes > requirements.txt

# Development stage
FROM base as dev

WORKDIR /app

ENV APP_ENV development
COPY --from=builder /app/requirements.txt /app/requirements.txt
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 9000
ENV PYTHONPATH "${PYTHONPATH}:/app"
CMD python /app/run.py