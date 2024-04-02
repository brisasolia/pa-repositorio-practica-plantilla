import modules.modulo1 as menuop

     #Se muestra el menú mientras la opción sea distinta a "5 - Salir"
def main():
      p_ordenada,f_ordenada=("./data/frases_de_peliculas.txt")

      opcion = 0
      while (opcion != 5):
            menuop.mostrar_opciones()
            opcion = int(input("Elige una opción: "))  
            if opcion == 1:
                  menuop.mostrarlistapeliculas(p_ordenada)
                  print ("\n" )
                  menuop(opcion)
                  
            elif opcion == 2:
                  menuop.trivia(p_ordenada, f_ordenada)
                  print ("\n" ) 
                  menuop(opcion)    
                  
            elif opcion == 3:
                  menuop.mostrarhistorial()
                  print ("\n" )
                  menuop(opcion)
                  
            #elif opcion == 4:
                  #menuop.borrarhistorial()
                  #menuop.guardarhistorial(opcion)
      
main ()