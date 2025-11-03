# Usamos la imagen oficial de Python 3.12
FROM python:3.12-slim

LABEL maintainer="Subgrupo 4 - FitCol"
LABEL description="Backend FitCol - Módulo de gestión de usuarios y rutinas"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecemos el directorio de trabajo
WORKDIR /app

# Instalamos las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el archivo de dependencias
COPY requirements.txt .

# Instalamos las dependencias de Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Creamos el directorio para la base de datos SQLite
RUN mkdir -p /app/data && \
    chmod 755 /app/data

# Exponemos el puerto en el que Flask va a correr
EXPOSE 5000

CMD ["python", "app.py"]