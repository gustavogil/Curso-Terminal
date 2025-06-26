# --- Importación de Librerías ---
import pandas as pd
import numpy as np

# --- Paso 1: Carga de Datos ---
nombre_archivo = 'compranet.csv'
print(f"Cargando datos desde '{nombre_archivo}'...")

try:
    # low_memory=False es una buena práctica para archivos grandes con columnas de tipos mixtos.
    df = pd.read_csv(nombre_archivo, low_memory=False)
    print(f"Éxito. Se cargaron {df.shape[0]} registros.")

    # Hacemos una copia para trabajar de forma segura
    df_limpio = df.copy()

    # --- Paso 2: Limpieza y Creación de la Columna 'Monto_Base' ---
    print("\n--- Normalizando Montos de Contrato a Valor Base (Sin IVA) ---")
    
    # Usamos los nombres de columna correctos que descubrimos
    monto_con_iva = pd.to_numeric(df_limpio['Total con IVA'].replace({r'\$': '', r',': ''}, regex=True), errors='coerce')
    monto_sin_iva = pd.to_numeric(df_limpio['Total Sin IVA'].replace({r'\$': '', r',': ''}, regex=True), errors='coerce')
    
    # Creamos la columna 'Monto_Base' con nuestra lógica de priorización
    df_limpio['Monto_Base'] = monto_sin_iva.fillna(monto_con_iva / 1.16)
    
    # --- Paso 3: Implementación de tu Estrategia (Eliminar Filas sin Monto) ---
    print(f"Número de filas antes de eliminar montos nulos: {len(df_limpio)}")
    df_limpio['Monto_Base'] = df_limpio['Monto_Base'].replace(0, np.nan)
    df_limpio.dropna(subset=['Monto_Base'], inplace=True)
    print(f"Número de filas después de la limpieza de montos: {len(df_limpio)}")

    # --- Paso 4: Normalización de Nombres de Dependencia ---
    print("\n--- Normalizando nombres de Dependencias para unificar duplicados ---")
    
    # Nos aseguramos de que toda la columna sea de tipo string
    df_limpio['Dependencia'] = df_limpio['Dependencia'].astype(str)
    
    # Usamos .str para acceder a los métodos de string y encadenarlos
    columna_limpia = df_limpio['Dependencia'].str.lower().str.replace('á', 'a').str.replace('é', 'e').str.replace('í', 'i').str.replace('ó', 'o').str.replace('ú', 'u').str.replace(',', '').str.replace('.', '')
    
    # Reemplazamos la columna original con nuestra versión limpia
    df_limpio['Dependencia'] = columna_limpia
    print("Nombres de dependencias normalizados.")

    # --- Paso 5: Análisis Final con Groupby ---
    print("\n--- Top 10 Dependencias por Monto Base Gastado (Análisis Definitivo) ---")
    
    monto_por_dependencia = df_limpio.groupby('Dependencia')['Monto_Base'].sum()
    top_10_monto = monto_por_dependencia.sort_values(ascending=False).head(10)

    print(top_10_monto)

except KeyError as e:
    print(f"\nERROR: No se encontró la columna necesaria: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")