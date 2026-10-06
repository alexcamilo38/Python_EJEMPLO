# asi se acceden los elementos de un dicciobario
diccionario = {'a': 1, 'b': 2, 'c':3}

for k, v in diccionario.items():
    print("Clave={0}", "Valor={1}".format(k,v))
    
    

# este es si solamente se requiere los valores
diccionario = {'a': 1, 'b': 2, 'c':3}

for v in diccionario.values():
    print( "Valor={0}".format(v))
    
    
    
# este es para saver solamente se requiese las claves las claves keys es para las claves
diccionario = {'a': 1, 'b': 2, 'c':3}

for k in diccionario.keys():
    print( "Clave={0}".format(k))
    
    