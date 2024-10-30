print("\nNombre: Ruvalcaba Valverde Miguel Angel")
print("-------recursida-------")
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
tri_recursion(6)
#tarde en enteder pero en resumen, es un contador o se puede usar como uno eso enenti yo
