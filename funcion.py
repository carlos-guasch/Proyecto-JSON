import json
with open('coches.json') as d:
  doc = json.load(d)
#1
#Para empezar hago un bucle y si hay coches en el documento le digo que haga un print del nombre del coche y en la siguiente linea muestro su origen. Si no hay coche hará un print de que no hay coches.
def lista_coches():
  print("")
  print("El nombre del coche y su origen:" )
  for l in doc:
    print(" ")
    print("-Titulo: "+(l['Name']))
    print("-Origen: "+(l['Origin']))
  if l==[]:
    print("")
    print("No hay coches disponibles en este archivo.")
#2
#Cuento los coches que hay, accidiendo al archivo de coche con la foncion len y despues hago un print con el resultado.
def cototales():
  coches = len(doc)
  print("El numero de coches disponibles en el documento son: "+str(coches))
#3
#Pido al usuario introducir un origen de un coche, accedemos al archivo json y ahi tenemos todos los coches y despues con el find accedo a cada coche y si el origen que puso el usuario es el mismo que tiene un coche del documento o contiene algun caracter igual que el origen introducido lo pone en una lista y hace el print de la lista. 
def origen():
  cad=input("Introduce un origen: ").lower()
  #.lower(): es para que busque ni diferenciar mayusculas ni minusculas.
  tcoches=[]
  for coche in doc:
    año=[]
    nom_lib = coche['Origin'].lower()
    if nom_lib.find(cad) >= 0:
        año.append(coche['Year'])
        tcoches.append((coche ['Name'],año))
  if tcoches==[]:
    print("No hay coches con la cadena introducida.")
  else:
    print("")
  print("El nombre del coche y el año es:" )
  print(" ")
  print("\n".join(map(str, tcoches)).replace('[','').replace("]",'').replace("'",'').replace('(','').replace(')','').replace(',',' -- '))
#4
#Pido al usuario introducir el nombre completo del coche, accedemos al archivo json y ahi tenemos todos los coches despues con el if name == nombre que introdujo el usuario, verifico que si el name de el usurio es igual al algun name del archivo y luego muestro los cilindros, si no existe en el archivo le dice al usuario que no existe.
def cilindro():
  cox=input("Introduce el nombre completo de un coche: ")
  cilin=[]
  for coche in doc:
    if coche['Name']==cox:
        cilin.append((coche ['Cylinders']))
        print("")
        print("El numero de cilindros del coche introducido es: "+" ".join(map(str, cilin)) )
  if cilin==[]:
    print("")
    print("Este coche no existe.")
#5
#Pido al usuario que introduzca un rango de caballos que tengan esos coches y despues accedemos al json y ahi tenemos todos los coches y despues verifico coche por coche si sus caballos estan dentro del rango introducido y despues los pongo en una lista y si hay algun libro dentro de la lista lo muetro, sino hago un print de que no hay coches con ese rango de caballos.
def caballos():
  cab_min=float(input("Caballos minimos: "))
  cab_max=float(input("Caballos maximos: "))
  caball=[]
  for coche in doc:
    cv = coche['Horsepower']
    if float(cv)>cab_min and float(cv)<cab_max:
      caball.append(coche ['Name'])
  if caball==[]:
    print("No hay ningun coche en este rango")
  else:
    print(" ")
    print("Los coches disponebles entre " + str(cab_min) +("cv") + " y " + str(cab_max) + "cv son: ")
    print(" ")
  for lib in caball:
    print("-",str(lib),str("\n"))
#6
def fin():
  print("Fin") 
  exit()
