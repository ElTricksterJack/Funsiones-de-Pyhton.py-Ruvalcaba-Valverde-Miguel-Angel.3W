print("\nNombre: Ruvalcaba Valverde Miguel Angel")
print("----------------Funciones-----------------")
print("Que es un funsion: Una función es un bloque de código que solo se ejecuta cuando se lo llama. \nPuede pasar datos, conocidos como parámetros, a una función. \nUna función puede devolver datos como resultado.")
#Uf tremendo copy paste, pero mejor lo explicare con mis propias palabras.
#Una funsion es un valor que tiene codigo ya asignao que puedes invocar a tu gusto, el ejemplo esta esta acontinuaion.
print("-----")
def FEDEX():#Funsion Experimetal Del Espesimen Xipetotec
  x = 12412+123
  print("One piece y undead unluck son lo mejor")
  print(x) #aqui esta el codigo de la funsion.
FEDEX()
#aqui invocamos el codigo de la funsion FEDX
from os import system
ok = input("Continuar?:") 
system("cls")
print("--------------Ejemplo-----------------")
print("--Imagina una funsion de esta manera--")
print("Funasion: Ritual antiguo para invocar demonios.")
print("Codigo de la Funsion: Demonio que se puede invocar.")
print("Para invocar invocar al demonio Reddoticantel, tienes que desir las palabras antiguas del ritual.")
def kilaquezoxt():
    print("El demonio Reddoticantel fue invocado")
print("kilaquezoxt")
kilaquezoxt()
print("y el demonio fue invocado, ese es el ejemplo. =P")
ok = input("Continuar?:") 
system("cls")
print("-------------Argumentos---------------")
def dreemurr(fname):
  print(fname + " Dreemurr")
#Esto se le llama argumentos, son varibles echas junto a la funsion y estos pueden ser cambiados por bariables ya establesidas.
dreemurr("Toriel")
dreemurr("Asgore")
dreemurr("Asriel")
dreemurr("Kris")
ok = input("Continuar?:") 
system("cls")
print("-------------Argumentos---------------")
def fname(nombre, apellido):
  print(nombre + " " + apellido)
fname("Nikola", "Tesla")
#fname("Nikola") #recuerda que si tienes 2 funsones, no puedes dejar una variable basia. amenos que... continuara dandadan
#Puedes haser mas de un argumento.
ok = input("Continuar?:") 
system("cls")
print("----Argumentos arbitrarios, *args-----")
def YJ(*vi):#YoJo
  print("yo juego " + vi[2])#se cuenta inisiando desde el 0
#amens que... si hay varias opsiones y programas el argumento de manera antisipada, si funsiona
YJ("Minegraft", "Roblox", "Dislyte")
ok = input("Continuar?:") 
system("cls")
print("----Argumentos de palabras clave-----")
def DDD(child3, child2, child1):#Desarolladores De Deltarun
  print("yo soy " + child3)
#Con esto puedes priorisar argumentos, o haser un argumento clave
DDD(child1 = "Temi", child2 = "Toby", child3 = "Nubert")
ok = input("Continuar?:") 
system("cls")
print("----Argumentos de palabras clave arbitrarias, **kwargs----")
def my_function(**kid):
  print("Mi apellido es " + kid["ape"])
#Aqui puedes escojer variables clave desde fuera o escribirlas desde afuera de la funsion.
my_function(name = "Toby", ape = "Fox")
ok = input("Continuar?:") 
system("cls")
print("----Valor del parámetro predeterminado----")
def my_function(country = "soy Goku"):
  print("yo soy " + country)
my_function("tu pader")
print("Y")
my_function("inevitable")
my_function()
print("Nota:Para entender vea el video porfabor.")
import webbrowser
webbrowser.open("https://www.youtube.com/shorts/wzob3c7fyiM")#https://www.youtube.com/shorts/wzob3c7fyiM
True
#si invesgie esto solo para que lo viera
#con esto se demuestra como podermos acumular cambiar argumentos y si hay un espasio disponible para el argumento predifinido se podra integrar
ok = input("Continuar?:") 
system("cls")
print("----Pasar una lista como argumento----")
def menu(comida):#vera con esto lo que hasemos es que integramos una lista a nuestra funsion
  for x in comida:
    print(x)
print("--los platillos exoticos son--")
exotico = ["Estofado de Dinosauro", "Costilla frita de Dragon", "Pizza Quimera"]
menu(exotico)
ok = input("Continuar?:") 
system("cls")
print("----------Valores de retorno----------")
def por(x):#Para permitir que una función devuelva un valor, utilice la return declaración
    return 5 * x
#en otras palabras, para que se muestre el valor de la funsion usa return, y hasi te ahoras la moslestia de haser variables. dandadan
print(por(3))
print(por(5))
print(por(9))
ok = input("Continuar?:") 
system("cls")
print("--------La Declaración de Pase--------")
def void():
  pass
#las funsiones que estan basias tiene que tener la palabra pass para que no alla errors. =)
#uf estoy muy cansaditto, pero tengo que continuar o sino sere un fracasaditto, y si pasa eso estar muy agutaditto.
#ademas no quiero estar despediditto, y eso me estaria estar procupaditto, pero estoy muy emosinaditto y sorprendiditto.
#hasi que continuare sin estar estresaditto... bueno ese no fue tan grasisos pero hay un pokemon que se llama ditto.
print("aqui no hay nada *eco* *eco mas bajo* *eco aun mas bajo* ")
print("-------Argumentos exclusivamente posicionales-------")
def fun(x, /):
  print(x)
#Puede especificar que una función puede tener SÓLO argumentos posicionales o SÓLO argumentos de palabras clave.
#Para especificar que una función solo puede tener argumentos posicionales, agregue , / después de los argumentos
fun(6)
print("\Comparen señores/")
#Sin embargo, , /en realidad se permite usar argumentos de palabras clave incluso si la función espera argumentos posicionales
def funfun(x):
  print(x)
funfun(x = 3)
ok = input("Continuar?:") 
system("cls")
print("-------Argumentos basados ​​únicamente en palabras clave-------")
def NotFun(*, x):
  print(x)
NotFun(x = 3)
#Para especificar que una función solo puede tener argumentos de palabras clave, agregue *, antes de los argumentos
print("\Comparen señores/")
def NotFunNotFun(x):
  print(x)
#Sin él, *, se permite utilizar argumentos posicionales incluso si la función espera argumentos de palabras clave
NotFunNotFun(3)
ok = input("Continuar?:") 
system("cls")
print("-------Argumentos basados ​​unicamente en palabras clave-------")
def F(a, b, /, *, c, d):
  print(a + b + c + d)
#Puede combinar los dos tipos de argumentos en la misma función.
#Cualquier argumento antes de / ,son solo posicionales, y cualquier argumento después de *, son solo palabras clave.
F(5, 6, c = 7, d = 8)
print("\ejemplo final/")
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("--Recursion--")
tri_recursion(6)
print("--------------------------------------")
print("Resultado: se comprendio sobre las funsiones y como usarlas.\n")
#Mr.Ink: saven algo, prefiero llamarlas invocasiones o tu que dises Menta?
#Menta: Tu sais quelque chose, je pense que ce sont de bonnes fonctions.
#Mink: ? eso es franses, ハハ、私は日本語の方が好きです
#Mel: pret,ilat osg'r je-lit?
#Mikaela:На каком языке это Мел?
#Mel: es Prviodetl Mikaela
#Mr.Ink: esto no es un juego, porfabor discutamos en la mente de M y no qui si entedieron pongan un punto. . . . . . . .
