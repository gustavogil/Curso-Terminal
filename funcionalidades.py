import pandas as pd

# 'pd' es el alias estándar que toda la comunidad de Python usa para pandas

# Imagina los datos de varias empresas que estás analizando para tu Search Fund
datos_empresas = {
    'Nombre': ['Empresa Alpha', 'Software Beta', 'Comercial Gamma'],
    'Industria': ['Manufactura', 'Tecnología', 'Retail'],
    'Facturacion_Anual_M': [120, 45, 80],
    'EBITDA_M': [15, 12, 9]
}

# Creamos el DataFrame a partir del diccionario
df_empresas = pd.DataFrame(datos_empresas)

print("\n--- Filtrando empresas con Facturación > 90M ---")

## La condición df_empresas['Facturacion_Anual_M'] > 90 crea una serie de True/False.
## Luego usamos esa serie para filtrar el DataFrame original.

col_facturacion = df_empresas['Facturacion_Anual_M']

empresas_grandes = df_empresas[col_facturacion > 90]

print(empresas_grandes)

##Empresas que sean de la Industria Tecnología

print("\n--- Filtrando empresas de la Industria Tecnología ---")

col_industria =df_empresas['Industria']

empresas_tecnologia = df_empresas[col_industria == "Tecnología"]

print(empresas_tecnologia)