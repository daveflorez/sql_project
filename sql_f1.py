import os
import pandas as pd
from sqlalchemy import create_engine

# Configura tu conexión
usuario = 'postgres'
contraseña = 'dave0201'
host = 'localhost'
puerto = '5432'
base_de_datos = 'f1db'

# Ruta donde están los CSV
directorio_csv = '/Users/davidflorez/Downloads/f1db-csv'

# Conexión a PostgreSQL
engine = create_engine(f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_de_datos}')

# Importar todos los CSV
for archivo in os.listdir(directorio_csv):
    if archivo.endswith('.csv'):
        ruta = os.path.join(directorio_csv, archivo)

        # Quitar prefijo, extensión y guiones
        nombre_tabla = os.path.splitext(archivo)[0]
        nombre_tabla = nombre_tabla.replace('f1db-', '').replace('-', '_').lower()

        print(f'Importando archivo: {archivo} → tabla: {nombre_tabla}')

        df = pd.read_csv(ruta)
        df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)

print("\n✅ Importación completada. Todas las tablas han sido reemplazadas.")