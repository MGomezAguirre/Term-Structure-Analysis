import pytest
import pandas as pd
import os
from termstruc.helper.save_data import save_data_to_csv
from termstruc.config import TICKERS
import numpy as np

def crear_df_prueba(tickers, num_filas=10):
    np.random.seed(0)  
    data = np.random.randn(num_filas, len(tickers))  # Datos aleatorios
    df_prueba = pd.DataFrame(data, columns=tickers)
    return df_prueba

@pytest.fixture
def archivo_temporal():
    """Fixture para crear y limpiar un archivo temporal."""
    file_path = 'data/test_save_data.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Asegurarse de que el directorio exista
    yield file_path
    if os.path.exists(file_path):
        os.remove(file_path)




def test_save_data_to_csv(archivo_temporal):
    # Definir la ruta del archivo CSV para la prueba
    file_path = archivo_temporal

    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

    # Llamar a la función para guardar el DataFrame
    save_data_to_csv(df, file_path)

    # Leer el archivo CSV y convertirlo en un DataFrame
    saved_df = pd.read_csv(file_path)

    # Comparar los DataFrames
    pd.testing.assert_frame_equal(df, saved_df, check_exact=False)

    # Limpiar el archivo CSV después de la prueba
    os.remove(file_path)