FROM python:3.9-slim

WORKDIR /app
COPY src/ /app/src/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "src/app.py"]
