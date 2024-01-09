FROM python:3.9-alpine

WORKDIR /app
COPY . .
RUN pip install python-dotenv

CMD ["python", "bot/main.py"]
