FROM python:3.10

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

COPY /app /app/app

WORKDIR /app/app

COPY secrets/secrets.env secrets/secrets.env

# Note: This not expose the port to the host machine, it for documentation purposes
EXPOSE 30000    

CMD ["python3", "main.py"]