# Aplicación principal
# Define el diccionario donde se almacenará la información
diccionario_peliculas = {}

# Abre el archivo en modo de lectura utilizando with open
#with open("data/frases_de_peliculas.txt", "r") as archivo:
    # Lee cada línea del archivo
    #for linea in archivo:
        # Elimina el salto de línea al final y luego divide la línea en función del punto y coma
        #frase, pelicula = linea.strip().split(";")
        
        # Guarda la información en el diccionario
        #diccionario_peliculas[pelicula] = frase

# Imprime el diccionario resultante
#print(diccionario_peliculas)


from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('templates/home.html')

if __name__=="__main__":
    app.run()