from flask import Flask, request, render_template, redirect, url_for #pip install Flask
import mysql.connector #pip install mysql-connector-python

app = Flask(__name__)

#Configiracion de conexcion de coneccion Mysql
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'flask_db'
}

@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM personas")
    personas = cursor.fetchall()
    cursor.close()
    return render_template('index.html', personas=personas)

@app.route('/agregar', methods = ['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO personas (nombre) VALUES (%s)", (nombre,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('agregar.html')


#@app.route('/buscar/<int:id>/personas')

if __name__ == '__main__':
    app.run(debug=True)