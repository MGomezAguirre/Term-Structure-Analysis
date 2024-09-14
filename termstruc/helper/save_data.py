
import pandas as pd
import os

def save_data_to_csv(df: pd.DataFrame, filename: str):
    # Asegurarse de que el directorio del archivo exista
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # Guardar el DataFrame en el archivo CSV
    df.to_csv(filename, index=False)