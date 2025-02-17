import matplotlib.pyplot as plt
import seaborn as sns
from data_processing import load_data

# Función para gráficos de distribución
def graficos_distribucion(df):
    caracteristicas = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    sns.set(style="whitegrid")

    for caracteristica in caracteristicas:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[caracteristica], kde=True, color="blue", bins=20)
        plt.title(f"Distribución de {caracteristica.upper()}", fontsize=14)
        plt.xlabel(caracteristica.capitalize(), fontsize=12)
        plt.ylabel("Frecuencia", fontsize=12)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

# Función para gráficos de caja (boxplot)
def graficos_boxplot(df):
    caracteristicas = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    sns.set(style="whitegrid")

    for caracteristica in caracteristicas:
        plt.figure(figsize=(12, 6))
        sns.boxplot(x="label", y=caracteristica, data=df, palette="viridis")
        plt.title(f"Boxplot de {caracteristica.upper()} por Cultivo", fontsize=14)
        plt.xlabel("Cultivo", fontsize=12)
        plt.ylabel(caracteristica.capitalize(), fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

# Función para la matriz de correlación (heatmap)
def matriz_correlacion(df):
    caracteristicas_numericas = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    matriz_corr = df[caracteristicas_numericas].corr(method="pearson")

    print("\nMatriz de Correlación de Pearson:")
    print(matriz_corr)

    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_corr, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, square=True)
    plt.title("Heatmap de la Matriz de Correlación (Pearson)", fontsize=14)
    plt.show()

if __name__ == "__main__":
    # Ruta del archivo CSV
    file_path = "../data/Crop_recommendation.csv"

    # Cargar los datos
    data = load_data(file_path)

    # Generar gráficos
    graficos_distribucion(data)
    graficos_boxplot(data)
    matriz_correlacion(data)
