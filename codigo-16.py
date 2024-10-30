print("\nNombre: Ruvalcaba Valverde Miguel Angel")
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
