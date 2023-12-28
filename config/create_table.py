import sqlite3

conn = sqlite3.connect('database/CentroSalud.db')
print("Connected succesfully")

"""conn.execute('CREATE TABLE Usuarios (code TEXT, password TEXT, email TEXT, password2 TEXT)')
print("Creates succesfully")
"""

conn.execute('CREATE TABLE Citas (nombre TEXT, edad TEXT, codigo TEXT,  fecha DATE)')
conn.commit()
conn.close()