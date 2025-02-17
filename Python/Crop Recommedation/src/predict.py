import pickle
import pandas as pd
import json
import os
import numpy as np
from datetime import datetime

# 📌 Cargar el modelo entrenado
modelo_path = "../models/mejor_modelo.pkl"
with open(modelo_path, "rb") as file:
    modelo = pickle.load(file)

# 📌 Definir rangos realistas de características
rangos = {
    "N": (0, 140),
    "P": (5, 145),
    "K": (5, 205),
    "temperature": (8, 43),
    "humidity": (14, 99),
    "ph": (3.5, 9),
    "rainfall": (20, 300)
}

# 📌 Generar datos aleatorios dentro de los rangos reales
nuevos_datos = pd.DataFrame({
    "N": [np.random.randint(*rangos["N"])],
    "P": [np.random.randint(*rangos["P"])],
    "K": [np.random.randint(*rangos["K"])],
    "temperature": [np.random.uniform(*rangos["temperature"])],
    "humidity": [np.random.uniform(*rangos["humidity"])],
    "ph": [np.random.uniform(*rangos["ph"])],
    "rainfall": [np.random.uniform(*rangos["rainfall"])]
})

print("\n🔍 Datos generados para predicción:")
print(nuevos_datos)

# 📌 Realizar la predicción
prediccion = modelo.predict(nuevos_datos)[0]

print(f"\n🌾 Cultivo recomendado: {prediccion}")

# 📌 Estructurar los datos para JSON
prediccion_json = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "input_data": nuevos_datos.to_dict(orient="records")[0],
    "predicted_crop": prediccion
}

# 📌 Definir ruta para guardar predicciones
json_path = "../predictions/predictions.json"

# 📌 Si el archivo no existe, crearlo vacío
if not os.path.exists(json_path):
    with open(json_path, "w") as file:
        json.dump([], file)

# 📌 Cargar JSON existente
with open(json_path, "r") as file:
    predicciones_previas = json.load(file)


print(f"\n💾 Predicción guardada en {json_path}")

