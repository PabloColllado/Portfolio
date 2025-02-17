import pandas as pd
from data_processing import load_data  # Importar la función para cargar los datos

# Ruta del archivo CSV (ajusta si es necesario)
file_path = "../data/Crop_recommendation.csv"

def mostrar_rangos_caracteristicas(df):
    """
    Muestra rangos, promedios y estadísticas clave de las características numéricas por cultivo.

    Parámetros:
    df (pandas.DataFrame): DataFrame con los datos de cultivos.

    Retorna:
    pd.DataFrame: Un DataFrame con los valores mínimos, máximos, rango y media por cultivo.
    """
    # Lista de características numéricas
    caracteristicas = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

    # Lista para almacenar datos resumen
    data_resumen = []

    # Título
    print("\n🌿 ANÁLISIS DE CARACTERÍSTICAS POR CULTIVO 🌿")
    print("=" * 80)

    for cultivo in sorted(df['label'].unique()):
        cultivo_data = df[df['label'] == cultivo]

        print(f"\n📊 Cultivo: {cultivo.upper()}")
        print("-" * 80)

        # Crear DataFrame con estadísticas para este cultivo
        resumen = []
        for caracteristica in caracteristicas:
            min_val = cultivo_data[caracteristica].min()
            max_val = cultivo_data[caracteristica].max()
            rango = max_val - min_val
            media = cultivo_data[caracteristica].mean()

            # Agregar datos a la lista
            resumen.append([caracteristica, min_val, max_val, rango, media])

            # Guardar datos en el resumen global
            data_resumen.append({
                "Cultivo": cultivo,
                "Característica": caracteristica,
                "Mínimo": min_val,
                "Máximo": max_val,
                "Rango": rango,
                "Media": media
            })

        # Convertir a DataFrame y mostrar con formato limpio
        df_resumen = pd.DataFrame(resumen, columns=["Característica", "Mínimo", "Máximo", "Rango", "Media"])
        print(df_resumen.to_string(index=False))

        # Destacar las características más importantes
        caracteristica_mayor_rango = df_resumen.loc[df_resumen["Rango"].idxmax(), "Característica"]
        mayor_rango_valor = df_resumen["Rango"].max()

        coef_var = {carac: (cultivo_data[carac].std() / cultivo_data[carac].mean()) * 100 for carac in caracteristicas}
        caracteristica_mas_variable = max(coef_var, key=coef_var.get)

        print("\n🔎 Resumen del Cultivo:")
        print(f"📌 Característica con mayor rango: {caracteristica_mayor_rango} (Rango: {mayor_rango_valor:.2f})")
        print(f"📌 Característica más variable: {caracteristica_mas_variable} (CV: {coef_var[caracteristica_mas_variable]:.2f}%)")
        print("-" * 80)

    # Convertir lista a DataFrame y devolver
    return pd.DataFrame(data_resumen)

if __name__ == "__main__":
    # Cargar los datos antes de ejecutar la función
    data = load_data(file_path)

    # Ejecutar el análisis
    df_resumen = mostrar_rangos_caracteristicas(data)

    # Opcional: Guardar el resumen en un CSV
    df_resumen.to_csv("../data/resumen_caracteristicas.csv", index=False)
