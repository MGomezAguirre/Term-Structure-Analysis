import pytest
import pandas as pd
from termstruc.config import TICKERS
from termstruc.src.descarga import descargar_datos_bonos

@pytest.fixture
def downloaded_data():
    """Fixture que descarga los datos una vez para todas las pruebas."""
    return descargar_datos_bonos()

def test_descarga_columnas(downloaded_data):
    open_df, close_df, volume_df = downloaded_data

    # Verificar que el número de columnas sea igual al número de tickers
    assert open_df.shape[1] >= round(len(TICKERS)*0.7), f"Se esperaban al menos {round(len(TICKERS)*0.7)} columnas, pero se obtuvieron {open_df.shape[1]}"
    assert close_df.shape[1] >= round(len(TICKERS)*0.7), f"Se esperaban al menos {round(len(TICKERS)*0.7)} columnas, pero se obtuvieron {close_df.shape[1]}"
    assert volume_df.shape[1] >= round(len(TICKERS)*0.7), f"Se esperaban al menos {round(len(TICKERS)*0.7)} columnas, pero se obtuvieron {volume_df.shape[1]}"

def test_sin_valores_nulos(downloaded_data):
    open_df, close_df, volume_df = downloaded_data

    # Verificar que no hay valores nulos en los DataFrames
    assert open_df.isnull().mean().mean() <= 0.7, f"Más del 50% de los datos son nulos ({open_df.isnull().mean().mean()*100:.2f}%)"
    assert close_df.isnull().mean().mean() <= 0.7, f"Más del 50% de los datos son nulos ({close_df.isnull().mean().mean()*100:.2f}%)"
    assert volume_df.isnull().mean().mean() <= 0.7, f"Más del 50% de los datos son nulos ({volume_df.isnull().mean().mean()*100:.2f}%)"
    
def test_dataframes_con_datos(downloaded_data):
    open_df, close_df, volume_df = downloaded_data

    # Verificar que los DataFrames contienen datos (es decir, tienen filas)
    assert open_df.shape[0] > 0, "open_df está vacío"
    assert close_df.shape[0] > 0, "close_df está vacío"
    assert volume_df.shape[0] > 0, "volume_df está vacío"
