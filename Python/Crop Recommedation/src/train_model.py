import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from data_processing import load_data  # Importamos la función para cargar los datos

# 📌 Ruta del archivo CSV
file_path = "../data/Crop_recommendation.csv"

def dividir_datos(df):
    X = df.drop(columns=["label"])  # Variables predictoras
    y = df["label"]  # Variable objetivo (cultivo recomendado)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("\n📌 División de Datos:")
    print(f"- Tamaño Train: {X_train.shape[0]} muestras")
    print(f"- Tamaño Test: {X_test.shape[0]} muestras")

    return X_train, X_test, y_train, y_test

def entrenar_modelos(X_train, y_train, X_test, y_test):
    modelos = {
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
        "DecisionTree": DecisionTreeClassifier(random_state=42),
        "SVM": SVC(kernel='linear', probability=True)
    }

    mejor_modelo = None
    mejor_nombre = None
    mejor_precision = 0.0

    print("\n🚀 Entrenando Modelos y Comparando Resultados...\n")

    for nombre, modelo in modelos.items():
        print(f"🔹 Entrenando modelo: {nombre} ...")
        modelo.fit(X_train, y_train)

        y_pred = modelo.predict(X_test)
        precision = accuracy_score(y_test, y_pred)

        print(f"🔹 Precisión de {nombre}: {precision:.4f}\n")
        print(classification_report(y_test, y_pred))

        if precision > mejor_precision:
            mejor_precision = precision
            mejor_modelo = modelo
            mejor_nombre = nombre

    print(f"\n🏆 Mejor Modelo: {mejor_nombre} con precisión {mejor_precision:.4f}\n")
    return mejor_modelo, mejor_nombre

def guardar_modelo(modelo, nombre_modelo, nombre_archivo="../models/mejor_modelo.pkl"):
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

    with open(nombre_archivo, "wb") as archivo:
        pickle.dump(modelo, archivo)
    
    print(f"\n💾 Mejor modelo guardado ({nombre_modelo}) en {nombre_archivo}")

if __name__ == "__main__":
    # Cargar datos
    data = load_data(file_path)

    # 🟢 Ahora `dividir_datos()` está definida antes de usarse
    X_train, X_test, y_train, y_test = dividir_datos(data)

    # Entrenar modelos y seleccionar el mejor
    mejor_modelo, mejor_nombre = entrenar_modelos(X_train, y_train, X_test, y_test)

    # Guardar el mejor modelo
    guardar_modelo(mejor_modelo, mejor_nombre)
