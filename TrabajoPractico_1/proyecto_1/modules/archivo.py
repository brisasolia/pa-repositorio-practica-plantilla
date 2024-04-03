def procesar_archivo():
    peliculas = set()
    frases_peliculas = {}
    with open("data/frases_de_peliculas.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            frase, pelicula = linea.strip().split(";")
            frases_peliculas.setdefault(pelicula.lower(), []).append(frase)
            peliculas.add(pelicula.lower().capitalize())  # Capitalizar la primera letra de cada película
    return list(peliculas), frases_peliculas