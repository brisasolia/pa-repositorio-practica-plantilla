# Aplicación principal

from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Función para procesar el archivo de frases de películas
def procesar_archivo():
    peliculas = set()
    frases_peliculas = {}
    with open("frases_de_peliculas.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            frase, pelicula = linea.strip().split(";")
            frases_peliculas.setdefault(pelicula.lower(), []).append(frase)
            peliculas.add(pelicula.lower())
    return list(peliculas), frases_peliculas

peliculas, frases_peliculas = procesar_archivo()

historial_resultados = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/juego', methods=['POST'])
def juego():
    num_frases = int(request.form['num_frases'])
    nombre_usuario = request.form['nombre_usuario']
    
    if num_frases < 3:
        return "El número de frases debe ser mayor o igual a 3."
    
    peliculas_elegidas = random.sample(peliculas, num_frases)
    frases_elegidas = {pelicula: random.choice(frases_peliculas[pelicula]) for pelicula in peliculas_elegidas}
    
    return render_template('juego.html', num_frases=num_frases, nombre_usuario=nombre_usuario, frases_elegidas=frases_elegidas)

@app.route('/listar_peliculas')
def listar_peliculas():
    return render_template('listar_peliculas.html', peliculas=sorted(peliculas))

@app.route('/resultados')
def resultados():
    return render_template('resultados.html', historial_resultados=historial_resultados)

if __name__ == '__main__':
    app.run(debug=True)

