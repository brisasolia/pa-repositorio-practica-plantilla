from flask import Flask, render_template, request, send_file
from modules import juego, archivo, graficas
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64


app = Flask(__name__)

peliculas, frases_peliculas = archivo.procesar_archivo() #en modulo aparte
ARCHIVO_USUARIOS = "usuarios.txt"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        num_frases = int(request.form['num_frases']) #salta error
        nombre_usuario = request.form['nombre_usuario']
        for _ in range(num_frases):
            return juego.iniciar_trivia(nombre_usuario, peliculas, frases_peliculas)  #modulo aparte para el juego
    else:
        return render_template('game.html')
    
@app.route('/listar_peliculas')
def listar_peliculas():
    return render_template('listar_peliculas.html', peliculas=sorted(peliculas))


@app.route("/mostrar_historial", methods=['GET'])
def mostrar_historial():
    try:
        with open(ARCHIVO_USUARIOS, "r") as f:
            datos_usuarios = [linea.strip().split(" - ") for linea in f]
    except FileNotFoundError:
        datos_usuarios = []

    graficas.generar_graficas(datos_usuarios)
    return render_template("historial.html", datos_usuarios=datos_usuarios) 


@app.route("/descargar_graficas", methods=['GET'])
def descargar_graficas():
    datos_usuarios = request.args.get('datos_usuarios') 
    pdf_buffer = graficas.generar_graficas(datos_usuarios)

    return send_file(
        pdf_buffer,
        attachment_filename="graficas.pdf",
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)

