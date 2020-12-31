# Imagen base para Python
FROM python:3.8-slim

# Copiar los archivos necesarios
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Ejecutaremos la consola del contenedor como punto de entrada
CMD [ "bin/sh" ]