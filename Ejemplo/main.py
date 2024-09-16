import pyodbc

# Ruta a tu base de datos Access (reemplaza con la ruta correcta)
db_path = r"C:/Users/JULIAN/OneDrive - Politécnico Grancolombiano/Escritorio/ejemplo.accdb"

# Cadena de conexión
conn_str = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={db_path};"
)

# Establecer conexión
conn = pyodbc.connect(conn_str)

# Crear un cursor
cursor = conn.cursor()

# Consulta SQL (ejemplo)
sql_query = "SELECT * FROM personal"

# Ejecutar consulta
cursor.execute(sql_query)

# Obtener resultados
rows = cursor.fetchall()

# Imprimir resultados (ejemplo)
for row in rows:
    print(row)

# Cerrar conexión
conn.close()