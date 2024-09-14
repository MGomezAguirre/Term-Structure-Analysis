
# poetry run python3 termstruc/main.py

from termstruc.src.descarga import descargar_datos_bonos, guardar_datos
#from termstruc.src.descarga_api import descargar_datos_api
#from termstruc.src.calcular_tir import calcular_tir, guardar_tir
#from termstruc.src.pca_analysis import aplicar_pca

def main():
    # Descargar datos
    open_df, close_df, volume_df = descargar_datos_bonos()
    descargar_datos_bonos('data/precios_bonos.csv')
 #   descargar_datos_api('data/datos_api.csv')
    
    # Calcular TIR
    precios_bonos = pd.read_csv('data/precios_bonos.csv')
 #   datos_api = pd.read_csv('data/datos_api.csv')
 #   tir = calcular_tir(precios_bonos, datos_api)
 #   guardar_tir(tir, 'data/tir.csv')
    
    # Aplicar PCA
 #   aplicar_pca('data/tir.csv', 'data/pc1.csv')

if __name__ == "__main__":
    main()
