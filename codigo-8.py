print("\nNombre: Ruvalcaba Valverde Miguel Angel")
print("----Argumentos de palabras clave arbitrarias, **kwargs----")
def my_function(**kid):
  print("Mi apellido es " + kid["ape"])
#Aqui puedes escojer variables clave desde fuera o escribirlas desde afuera de la funsion.
my_function(name = "Toby", ape = "Fox")
print("Resultado: se escojio la variable corepta.\n")
