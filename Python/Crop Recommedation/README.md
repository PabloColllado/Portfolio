# 🌱 Crop Recommendation - Proyecto de Machine Learning

## 📌 Descripción
Este proyecto utiliza **Machine Learning** para ayudar a los agricultores a identificar el cultivo más adecuado según las condiciones del suelo y el clima.
Para ello, analizamos datos relacionados con nutrientes, temperatura, humedad, pH y precipitaciones, entrenando un modelo de **Random Forest** que permite hacer recomendaciones precisas.
Además, probamos diferentes algoritmos de clasificación para comparar su rendimiento y seleccionar el más eficiente, asegurando así predicciones confiables y útiles para la toma de decisiones..  

---

## 📊 **Estructura del Proyecto**
```
Crop Recommendation/
│── README.md                  # 📄 Este archivo
│── requirements.txt            # 📦 Dependencias del proyecto
│
├── data/                       # 📊 Datos de entrenamiento
│   ├── Crop_recommendation.csv # 📂 Dataset original
│   ├── resumen_caracteristicas.csv # 📂 Estadísticas descriptivas
│
├── models/                     # 🧠 Modelos entrenados
│   ├── mejor_modelo.pkl        # ✅ Mejor modelo guardado
│
│
├── predictions/                 # 📄 Predicciones generadas
│   ├── predictions.json        # 📂 Historial de predicciones
│
├── src/                         # 📝 Código fuente del proyecto
│   ├── data_processing.py       # 🔄 Carga y limpieza de datos
│   ├── data_analysis.py         # 📊 Análisis estadístico
│   ├── data_visualization.py    # 📉 Gráficos y visualización
│   ├── train_model.py           # 🤖 Entrenamiento del modelo
│   ├── predict.py               # 🔮 Predicciones con nuevos datos
│
└── scripts/                     # 🏗️ Automatización del pipeline
    ├── run_pipeline.bat         # ▶️ Script para Windows
    ├── run_pipeline.sh          # ▶️ Script para Linux/Mac
```

---

## 🚀 **Cómo Usar el Proyecto**
### **1️⃣ Configurar el Entorno**
Asegúrate de tener **Python 3.x** y crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
```

### **2️⃣ Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### **3️⃣ Ejecutar el Pipeline Completo**
Ejecuta el script para procesar datos, entrenar el modelo y hacer predicciones:
```bash
cd scripts
run_pipeline.bat    # (Windows)
```

### **4️⃣ Hacer una Predicción Manualmente**
```bash
python src/predict.py
```

---

## 📊 **Modelos Usados**
| Modelo           | Precisión |
|-----------------|-----------|
| 🌳 Random Forest | **99.55%** |
| 🌲 Decision Tree | 89% |
| 🔗 SVM          | 91% |

🔹 **Random Forest fue seleccionado como el mejor modelo y guardado en `models/mejor_modelo.pkl`**.

---

## 💾 **Predicciones Guardadas en JSON**
Cada predicción se almacena en `predictions/predictions.json` con este formato:
```json
[
    {
        "timestamp": "2024-02-13 14:30:45",
        "input_data": {
            "N": 78,
            "P": 34,
            "K": 100,
            "temperature": 26.5,
            "humidity": 78.9,
            "ph": 6.5,
            "rainfall": 150.4
        },
        "predicted_crop": "rice"
    }
]
```

---


