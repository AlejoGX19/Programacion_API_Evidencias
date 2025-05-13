from flask import Flask, render_template # pip install Flask
from modulos import reporte #, otro,otro,otro
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/reporte")
def modulo_reportes():
    return reporte.mostrar_reportes()

if __name__ == "__main__":
    app.run(debug=True)