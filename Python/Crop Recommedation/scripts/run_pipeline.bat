@echo off
echo ===========================================
echo 🚀 Iniciando el pipeline de Machine Learning...
echo ===========================================

echo 🔹 Procesando los datos...
python ../src/data_processing.py

echo 🔹 Analizando los datos...
python ../src/data_analysis.py

echo 🔹 Entrenando el modelo...
python ../src/train_model.py

echo 🔹 Realizando predicciones...
python ../src/predict.py

echo ✅ Pipeline completado con éxito.
pause
