#Aqui importo el achivo que tiene todas las funcciones.
import funcion


#Aqui he creado un menu que da 5 opciones y despues te pide que escojas una de las 5, he hecho un bucle por si no escojes ninguna te vuelve a mostrar el menu ya la pregunta otra vez.
ans=True
#Menu
while ans:
    print ("""
    1.Mostrar lista de todos los coches.
    2.Mostrar el numero de coches que hay.
    3.Mostrar los nombres de coches con su año de fabricacion de un origen especfico.
    4.Mostrar los cilindros de un coche especifico. 
    5.Mostrar los nombres de coches dentro de un rango de caballos.
    6.Salir
    """)
    ans=input("Elige una opcion>>" )
    #Aqui importo las funciones que estan en el archivo de funciones.
    if ans=="1":
      funcion.lista_coches() 
    elif ans=="2":
      funcion.cototales() 
    elif ans=="3":
      funcion.origen()
    elif ans=="4":
      funcion.cilindro()    
    elif ans=="5":
      funcion.caballos()
    elif ans=="6":
      funcion.fin()
    #si introduce un numero que no esta en el menu le saldra el siguiente mensaje
    elif ans !="":
      print("\n Opcion no valida intentalo otra vez") 
