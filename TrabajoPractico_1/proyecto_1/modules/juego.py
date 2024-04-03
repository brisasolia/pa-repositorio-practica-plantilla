import random
from flask import render_template

def iniciar_trivia(nombre_usuario, peliculas, frases_peliculas):
    frases_seleccionadas = []
    mostrar_resultado = True
    punt = 0
    peliculas_elegidas = set()
    respuesta = ""
    pelicula = random.choice(peliculas)
    if pelicula not in peliculas_elegidas:
        frase = random.choice(frases_peliculas[pelicula])
        opciones = [p for p in peliculas if p != pelicula]
        opciones = random.sample(opciones, 2)
        opciones.append(pelicula)
        random.shuffle(opciones)
        frases_seleccionadas.append({'frase': frase, 'respuesta_correcta': pelicula, 'opciones': opciones})
        peliculas_elegidas.add(pelicula)
        
        if frases_seleccionadas[-1]['respuesta_correcta'] == frases_seleccionadas[-1]['opciones'][0]:
            respuesta = "¡Felicidades! Elegiste la opción correcta"
            punt += 1
        else:
            respuesta = "Fallaste, la respuesta correcta era: " + frases_seleccionadas[-1]['respuesta_correcta']
    return render_template('game.html', nombre_usuario=nombre_usuario, frase=frase, opciones=opciones, mostrar_resultado=mostrar_resultado, respuesta=respuesta, punt=punt)