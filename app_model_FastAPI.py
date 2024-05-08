from fastapi import FastAPI
import sqlite3
import pickle
import uvicorn
import pandas as pd

app = FastAPI()

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()


@app.get('/')
async def home():
    return "Bienvenido a mi API del modelo advertising"

# 1. Endpoint que devuelva la predicción de los nuevos datos enviados mediante argumentos en la llamada
@app.get("/predict")
async def predict(data: dict):

    model = pickle.load(open('data/advertising_model.pkl', 'rb'))
    
    prediction = model.predict([[data['data'][0][0], data['data'][0][1], data['data'][0][2]]])
    return {'prediction': round(prediction[0], 2)}

# 2. Endpoint para almacenar nuevos registros en la base de datos
@app.post("/ingest")
async def ingest(data: dict):
    
    for value in data['data']:
        cursor.execute('''INSERT INTO sales (tv, radio, newspaper, sales)
                          VALUES (?,?,?,?)''', 
                          (value[0], value[1], value[2], value[3])
                          )
        conn.commit()
    return {'message': 'Datos ingresados correctamente'}




# 3. Endpoint para reentrenar de nuevo el modelo con los posibles nuevos registros que se recojan
@app.post("/retrain")
async def retrain():
    model = pickle.load(open('data/advertising_model.pkl', 'rb'))

    # Con esta función leemos los datos y lo pasamos a un DataFrame de Pandas
    def sql_query(query):

        # Ejecuta la query
        cursor.execute(query)

        # Almacena los datos de la query 
        ans = cursor.fetchall()

        # Obtenemos los nombres de las columnas de la tabla
        names = ['tv', 'radio', 'newspaper', 'sales']

        return pd.DataFrame(ans,columns=names)
    
    query = '''
            SELECT * 
            FROM sales;
            '''

    df = sql_query(query)

    Xtrain = df[['tv','radio','newspaper']]
    ytrain = df['sales']

    model.fit(Xtrain, ytrain)

    return {'message': 'Modelo reentrenado correctamente.'}


# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

