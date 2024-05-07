# API de Predicción de Ventas

Esta es una API construida con FastAPI que proporciona endpoints para predecir ventas, almacenar nuevos registros en una base de datos y reentrenar el modelo de predicción de ventas.

## Despliegue de la API

Para ejecutar la aplicación localmente, sigue estos pasos:

1. Clona este repositorio:
ahttps://github.com/aliciamb86/APIs.git

2. Instala las dependencias:
pip install -r requirements.txt

3. Ejecuta la aplicación:
uvicorn main:app --host 127.0.0.1 --port 8000

## Endpoints

### 1. Predicción de Ventas

Endpoint para obtener la predicción de ventas dados los datos de inversión en publicidad.

- **URL**: `/predict`
- **Método**: GET
- **Parámetros**: 
  - `data`: Datos de inversión en publicidad (dict)

### 2. Ingesta de Datos

Endpoint para almacenar nuevos registros de ventas en la base de datos.

- **URL**: `/ingest`
- **Método**: POST
- **Parámetros**: 
  - `data`: Datos de ventas (dict)

### 3. Reentrenamiento del Modelo

Endpoint para reentrenar el modelo de predicción de ventas con los nuevos datos recolectados.

- **URL**: `/retrain`
- **Método**: POST

## Ejemplos de Uso

A continuación se muestran ejemplos de cómo utilizar los endpoints:

### Predicción de Ventas

```python
import requests

url = 'http://localhost:8000/predict'  
data = {'data': [[100, 100, 200]]} 
    
response = requests.get(url, json=data)
print(response.json())

