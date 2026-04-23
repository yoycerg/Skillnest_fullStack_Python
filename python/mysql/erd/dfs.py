inventario = {
   "frutas": ["manzana", "pera"],
   "verduras": ["zanahoria", "lechuga"]
}

for categoria, lista in inventario.items():
   print(categoria)
   for item in lista:
       print(item)
