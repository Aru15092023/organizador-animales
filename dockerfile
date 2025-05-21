# Usa una imagen base de Python que incluya las bibliotecas necesarias para Tkinter
# python:3.9-slim-buster es buena, pero puede que necesitemos instalar tk-dev si no está preinstalado.
# Una imagen completa de python:3.9 puede ser más fácil para empezar, aunque más grande.
# Optaremos por una base slim y añadiremos las dependencias de Tkinter.
FROM python:3.9-slim-buster

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala las dependencias de Tkinter y otras utilidades gráficas
# Esto es crucial para que Tkinter funcione en un entorno sin cabeza
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-tk \
    libxkbcommon-x11-0 \
    xauth \
    libnss3 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm-dev \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libgl1 \
    libgbm1 \
    libnspr4 \
    libxcb-dri3-0 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    libdbus-glib-1-2 && \
    rm -rf /var/lib/apt/lists/*

# Copia tu archivo de requisitos (si tienes otros módulos pip)
COPY requirements.txt .

# Instala las dependencias de Python listadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || true # '|| true' para no fallar si requirements.txt está vacío

# Copia tu aplicación Python al directorio de trabajo
COPY animales.py .

# Comando para ejecutar la aplicación Tkinter
# pasar la variable DISPLAY cuando se ejecute el contenedor.
CMD ["python", "animales.py"]