'''
Actividad  Gestor de inventario
'''
'''
1.- Creación: Crear una lista llmada inventario que contenga los siguientes
 articulos: "laptop", "ratón", "monitor", "cable hdmi"
'''
inventario = ["laptop", "teclado", "ratón", "monitor", "cable hdmi"]
'''
2 - Expanción_ Utiliza el método correspondientes para agregar "impresora"
al final de la lista '''
                                                                                           
inventario.append("impresora")
'''

 
3.- Conteo: Utiliza la funcion integrada para mostrar cuantos elementos totales hay en la lista. '''
print(len(inventario))

'''
4.- Acceso y modificación: Modifica "teclado" por "teclado mecánico". '''
inventario[1] = "teclado mecanico"
''' 
5.-  Slicing: Cre una nueva lista llamada "promoción" debe contener solo los 3 primeros elementos de la lista "inventario",
solo los 3 primeros elementos de la lista "inventario".'''
promocion = inventario[0:3]
'''
6.- Mostrar la lista de inventario ordenado alfabeticamente.'''
inventario.sort()
print(inventario)
'''
7.- Elimina el último elemento de la lista de inventario mostrando el elemento elimando y la lista final.'''

elemento_eliminado = inventario.pop()
print("Elemento elimanado", elemento_eliminado)