import sqlite3

conn = sqlite3.connect('database/CentroSalud.db')

cursor = conn.cursor()


code1 = '2215220308'
password1 = '1234ga'
email = 'bapoclinh@unac.edu.pe'
password21 = 'destroyer12'

cursor.execute('INSERT INTO Usuarios (code, password, email, password2) VALUES (?, ?, ?, ?)', (code1, password1, email, password21))

code2 = '2115220034'
password2 = '265rt'
email2 = 'jgtorresg@unac.edu.pe'
password22 = 'peru21'

cursor.execute('INSERT INTO Usuarios (code, password, email, password2) VALUES (?, ?, ?, ?)', (code2, password2, email2, password22))

conn.commit()

print("Data inserted succesfully")

conn.close 