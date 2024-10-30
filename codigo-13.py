print("\nNombre: Ruvalcaba Valverde Miguel Angel")
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
