# Aplicación principal

from flask import Flask, render_template, request
import random
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64


app = Flask(__name__)

# Función para procesar el archivo de frases de películas
def procesar_archivo():
    peliculas = set()
    frases_peliculas = {}
    with open("data/frases_de_peliculas.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            frase, pelicula = linea.strip().split(";")
            frases_peliculas.setdefault(pelicula.lower(), []).append(frase)
            peliculas.add(pelicula.lower())
    return list(peliculas), frases_peliculas

peliculas, frases_peliculas = procesar_archivo()

historial_resultados = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/game', methods=['POST', 'GET'])
def juego():
    if request.method=='POST':
    #num_frases=int("ingrese el número de frases: ")
        num_frases = int(request.form['num_frases'])
        nombre_usuario = request.form['nombre_usuario']
    
#    if num_frases < 3:
#      return "El número de frases debe ser mayor o igual a 3."
    
        peliculas_elegidas = random.sample(peliculas, num_frases)
        frases_elegidas = {pelicula: random.choice(frases_peliculas[pelicula]) for pelicula in peliculas_elegidas}
    
    return render_template('game.html', num_frases=num_frases, nombre_usuario=nombre_usuario, frases_elegidas=frases_elegidas)

@app.route('/game', methods=['GET', 'POST'])
#def game():
    #if request.method == 'POST':
       # num_frases = int(request.form['num_frases'])
        #nombre_usuario = request.form['nombre_usuario']
        
        #peliculas_elegidas = random.sample(peliculas, num_frases)
    #    frases_elegidas = {pelicula: random.choice(frases_peliculas[pelicula]) for pelicula in peliculas_elegidas}
        
    #    return render_template('game.html', num_frases=num_frases, nombre_usuario=nombre_usuario, frases_elegidas=frases_elegidas)
   # else:
    #    return render_template('game.html')

@app.route('/listar_peliculas')
def listar_peliculas():
    return render_template('listar_peliculas.html', peliculas=sorted(peliculas))

@app.route('/resultados')
def resultados():
    return render_template('resultados.html', historial_resultados=historial_resultados)


@app.route('/game', methods=['POST'])
def game():
    num_frases = int(request.form['num_frases'])
    nombre_usuario = request.form['nombre_usuario']
    
    if num_frases < 3:
        return "El número de frases debe ser mayor o igual a 3."
    
    frases_elegidas = []
    peliculas_elegidas = set()
    while len(frases_elegidas) < num_frases:
        pelicula = random.choice(peliculas)
        if pelicula not in peliculas_elegidas:
            frase = random.choice(frases_peliculas[pelicula])
            opciones = [p for p in peliculas if p != pelicula]
            opciones = random.sample(opciones, 2)
            opciones.append(pelicula)
            random.shuffle(opciones)
            frases_elegidas.append({'frase': frase, 'respuesta_correcta': pelicula, 'opciones': opciones})
            peliculas_elegidas.add(pelicula)
    
    return render_template('game.html', nombre_usuario=nombre_usuario, frases_elegidas=frases_elegidas)




@app.route('/resultados', methods=['POST'])
def resultado():
    respuesta_correcta = request.form['respuesta_correcta']
    opcion_elegida = request.form['opcion']
    if opcion_elegida.lower() == respuesta_correcta.lower():
        mensaje = "¡Felicidades! Has acertado."
    else:
        mensaje = f"¡Incorrecto! La respuesta correcta es: {respuesta_correcta}."
    return render_template('resultados.html', mensaje=mensaje)

@app.route('/resultado_final', methods=['POST'])
def resultado_final():
    aciertos = int(request.form['aciertos'])
    total_frases = int(request.form['total_frases'])
    historial_resultados.append((aciertos, total_frases, datetime.now(), request.form['nombre_usuario']))
    return render_template('resultado_final.html', aciertos=aciertos, total_frases=total_frases)

@app.route('/lista_resultados')
def lista_resultados():
    return render_template('lista_resultados.html', historial_resultados=historial_resultados)

@app.route('/graficas')
def graficas():
    return render_template('graficas.html')

@app.route('/descargar_graficas')
def descargar_graficas():
    # Código para generar las gráficas usando Matplotlib
    # Guarda las gráficas en BytesIO y luego convierte a base64
    output = BytesIO()
    plt.savefig(output, format='pdf')
    output.seek(0)
    graficas_base64 = base64.b64encode(output.getvalue()).decode()
    return render_template('descargar_graficas.html', graficas_base64=graficas_base64)

if __name__ == '__main__':
    app.run(debug=True)

