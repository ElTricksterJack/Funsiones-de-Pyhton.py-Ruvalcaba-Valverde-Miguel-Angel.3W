print("\nNombre: Ruvalcaba Valverde Miguel Angel")
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
#Mr.Ink: saven algo, prefiero llamarlas invocasiones o tu que dises Menta?
#Menta: Tu sais quelque chose, je pense que ce sont de bonnes fonctions.
#Mink: ? eso es franses, ハハ、私は日本語の方が好きです
#Mel: pret,ilat osg'r je-lit?
#Mikaela:На каком языке это Мел?
#Mel: es Prviodetl Mikaela
#Mr.Ink: esto no es un juego, porfabor discutamos en la mente de M y no qui si entedieron pongan un punto. . . . . . . .
