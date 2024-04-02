# módulo para organizar funciones o clases utilizadas en nuestro proyecto

import random
from flask import Flask, render_template, request


def mostrar_opciones():
    OPCIONES = """
    #######################################
    #  Películas: Preguntas y respuestas  #
    #######################################
    Elige una opción
    1 - Mostrar lista de películas.
    2 - ¡Trivia de película!
    3 - Mostrar secuencia de opciones seleccionadas previamente.
    4 - Borrar historial de opciones.
    5 - Salir

    """
    print(OPCIONES)

    def mostrarlistapeliculas(p_ordenada):
        for i in range(len(p_ordenada)):
            p_ordenada[i] = p_ordenada[i].lower()
    
    lista_no_repetida = []

    [lista_no_repetida.append(pelicula) for pelicula in p_ordenada if pelicula not in lista_no_repetida]

    for k in range(len(lista_no_repetida)):
        lista_no_repetida[k] = lista_no_repetida[k].title()
        print(k+1, lista_no_repetida[k])
    

def trivia(p_ordenada ,  f_ordenada):
    q=0
    print("¡Jugamos?")
    op=input()
    while op=="si":
         
         q=random.randint(0,len(f_ordenada)-1)    
         print("La frase es la siguiente: ",f_ordenada[q]) #mostramos la frase 
    
         opcionestrivia=[]        
         opcionestrivia.append(p_ordenada[q]) #agregamos la opción correcta
    
                         #agregamos al azar dos opciones más que no coincidan con la opción correcta 
    
         contador=0
         aleatorio2=q
    
         while contador<2:
                 aleatorio=random.randint(0,len(f_ordenada)-1)
                 if aleatorio!=q and aleatorio2!=aleatorio:
                     opcionestrivia.append(p_ordenada[aleatorio])
                     contador+=1
                     aleatorio2=aleatorio
         fa=-1
         fr=-1
         contador2=0
    
                 #mostramos las películas en un orden aleatorio 
    
         orden_muestreo=[]
    
         while contador2<3:
             f=random.randint(0,2)
             if f!=fa and fr!=f:      
                 print(f'{contador2+1} {opcionestrivia[f]}')
                 orden_muestreo.append(opcionestrivia[f])
                 fr=fa
                 fa=f
                 contador2+=1
    
         user=int(input("¿A qué película pertenece la frase? "))
   
    
         if orden_muestreo[user-1]==p_ordenada[q]:
             print ("\nFelicidades! Elegiste la opción correcta")
         else:
             print(f'\nERROR! La frase pertenece a {p_ordenada[q]}')
    
  
    
         cont=input("¿Desea seguir jugando? (si/no) ") 
         if cont=="si":
             op="si"
         else:
             op="no"