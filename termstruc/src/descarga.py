import pandas as pd
import yfinance as yf
from datetime import datetime
from termstruc.helper.save_data import save_data_to_csv
from termstruc.config import TICKERS


def descargar_datos_bonos():

    open_df = pd.DataFrame()
    close_df = pd.DataFrame()
    volume_df = pd.DataFrame()

    for ticker_symbol in TICKERS:
        ticker = yf.Ticker(ticker_symbol)
        data = ticker.history(period='1d', interval='5m')
        
        if not data.empty:
            open_df[ticker_symbol] = data['Open']
            close_df[ticker_symbol] = data['Close']
            volume_df[ticker_symbol] = data['Volume']
    
    return open_df, close_df, volume_df

def guardar_datos(open_df, close_df, volume_df):
    # Guardar los DataFrames en archivos CSV
    save_data_to_csv(open_df, 'bonos_open.csv')
    save_data_to_csv(close_df, 'bonos_close.csv')
    save_data_to_csv(volume_df, 'bonos_volume.csv')