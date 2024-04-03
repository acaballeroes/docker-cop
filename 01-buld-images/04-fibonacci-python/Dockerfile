# Usa una imagen oficial de Python como base
FROM python:3.8

WORKDIR /app

COPY /src /app

# Install dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "app.py"]
