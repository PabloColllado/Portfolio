import pandas as pd 

file_path = "C:/Users/pablo/OneDrive/Escritorio/Portfolio/Python/Crop Recommedation/data/Crop_recommendation.csv"

def load_data(file_path):
    data = pd.read_csv(file_path)
    print("Dataset cargado con éxito.")
    print(f"Filas: {data.shape[0]}, Columnas: {data.shape[1]}")
    print("\nPrimeras 5 filas del dataset:")
    print(data.head())
    return data

def revisar_valores_faltantes(df):
    print("\n" + "="*80)
    print("REVISIÓN DE VALORES FALTANTES")
    print("="*80)
    valores_faltantes = df.isnull().sum()
    print(valores_faltantes[valores_faltantes > 0])

    if valores_faltantes.sum() == 0:
        print("No hay valores faltantes en el dataset.")
    else:
        print("\nHay valores faltantes en las columnas listadas arriba.")


def generar_tablas_resumen(df):
    """
    Genera tablas resumen con estadísticas descriptivas para cada característica agrupada por cultivo.

    """
    # Lista de características numéricas a analizar
    caracteristicas = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

    print("\n" + "="*80)
    print("TABLAS RESUMEN AGRUPADAS POR CULTIVO")
    print("="*80)

    for caracteristica in caracteristicas:
        print(f"\n{'-'*80}")
        print(f"Estadísticas para: {caracteristica.upper()}")
        print(f"{'-'*80}")

        # Generar estadísticas descriptivas agrupadas por cultivo
        resumen = df.groupby('label')[caracteristica].describe()

        # Calcular rango y coeficiente de variación (CV)
        resumen['rango'] = resumen['max'] - resumen['min']
        resumen['cv (%)'] = (resumen['std'] / resumen['mean']) * 100

        # Renombrar columnas para legibilidad
        resumen = resumen.rename(columns={
            'count': 'Cantidad',
            'mean': 'Media',
            'std': 'Desv. Estándar',
            'min': 'Mínimo',
            '25%': 'Perc. 25',
            '50%': 'Mediana',
            '75%': 'Perc. 75',
            'max': 'Máximo',
            'rango': 'Rango',
            'cv (%)': 'CV (%)'
        })

        # Mostrar tabla en consola
        print(resumen)

        # Observaciones clave
        print("\nObservaciones:")
        print(f"• Cultivo con mayor {caracteristica}: {resumen['Máximo'].idxmax()} ({resumen['Máximo'].max():.2f})")
        print(f"• Cultivo con menor {caracteristica}: {resumen['Mínimo'].idxmin()} ({resumen['Mínimo'].min():.2f})")
        print(f"• Cultivo más variable en {caracteristica} (CV más alto): {resumen['CV (%)'].idxmax()} ({resumen['CV (%)'].max():.2f}%)")
        print(f"• Cultivo más consistente en {caracteristica} (CV más bajo): {resumen['CV (%)'].idxmin()} ({resumen['CV (%)'].min():.2f}%)")







if __name__ == "__main__":
    data = load_data(file_path)
    revisar_valores_faltantes(data)
    generar_tablas_resumen(data)
