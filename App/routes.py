from flask import render_template, request, redirect, url_for, session, make_response
from App import app
import sqlite3
from App.email_sender import EmailSender
from datetime import datetime

@app.route('/')
def home():
    response = make_response(redirect('/login'))
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = sqlite3.connect('database/CentroSalud.db')
        cursor = conn.cursor()

        code = request.form.get('code')
        password = request.form.get('password')
        email = request.form.get('mail')
        password2 = request.form.get('password2')

        query = "SELECT * FROM Usuarios WHERE (code=? AND password=?) OR (email=? AND password2=?)"
        cursor.execute(query,(code, password, email, password2))
        results = cursor.fetchall()

        if len(results) == 0:
            print("Intente nuevamente")
        else:
            return redirect(url_for('principal'))
        
    return render_template('login.html')


@app.route('/forgot_password', methods=['GET','POST'])
def forgot():
    if request.method == 'POST':
        conn = sqlite3.connect('database/CentroSalud.db')
        cursor = conn.cursor()

        f_code = request.form.get('f_code')
        f_email = request.form.get('f_email')
        facultades = request.form.get('facultades')

        query = "SELECT password, password2 FROM Usuarios WHERE code=? AND email=?"
        cursor.execute(query, (f_code, f_email))
        results = cursor.fetchall()

        if len(results) == 0:
            print("Intente nuevamente")
        else:
            
            password, password2 = results[0]
            
            remitente = "poclinbryan@gmail.com"
            passw = 'qngv kwby chwr izjz'
            servidor_smtp = 'smtp.gmail.com'
            puerto_smtp = 587
            
            email_sender = EmailSender(remitente, passw, servidor_smtp, puerto_smtp)
            
            destinatario = f'{f_email}'
            asunto = 'RECUPERACIÓN DE CONTRASEÑA'
            mensaje = f'Estimado estudiante de la {facultades}, la contraseña para ingresar con su código es: {password} y la contraseña para ingresar con su correo es: {password2}'
            
            email_sender.enviar_correo(destinatario, asunto, mensaje)

            return redirect(url_for('login'))

    return render_template('forgot_password.html')

@app.route('/principal')
def principal():
    return render_template('principal.html')

@app.route('/obtener_contenido/<menu_item_id>')
def obtener_contenido(menu_item_id):
    return render_template(f'{menu_item_id}.html')

@app.route('/agendar_cita', methods=['GET', 'POST'])
def agendar_cita():
    if request.method == 'POST':
        nombre = request.form.get('nombres')
        edad = request.form.get('edad')
        codigo = request.form.get('codigo')
        fecha_cita = request.form.get('fecha')
        
        fecha_cita_obj = datetime.strptime(fecha_cita, '%Y-%m-%d')
        fecha_cita_str = fecha_cita_obj.strftime('%Y-%m-%d')
        
        conn = sqlite3.connect('database/CentroSalud.db')
        cursor = conn.cursor()
        
        query_disponibilidad = "SELECT codigo FROM Citas WHERE fecha=?" 
        cursor.execute(query_disponibilidad, (fecha_cita_str,))
        fecha_ocupada = cursor.fetchone()
        
        if fecha_ocupada is not None:
            return render_template('agendacion.html')
        else:
            query_insertar = ('INSERT INTO Citas (nombre, edad, codigo, fecha) VALUES (?, ?, ?, ?)')
            cursor.execute(query_insertar, (nombre, edad, codigo, fecha_cita_str))
            conn.commit()
            conn.close()
            
            return redirect(url_for('principal'))
        
    return render_template('agendacion.html')

@app.route('/logout')
def logout():
    session.pop('code', None)
    return redirect(url_for('login'))

