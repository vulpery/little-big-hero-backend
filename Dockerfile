FROM python:3.10-slim-buster

RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /app

# Copy the requirements file into the container
COPY ./pyproject.toml .

# Install dependencies
RUN poetry install --only main
# Copy the rest of the application code
COPY . .

COPY .env .env

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
