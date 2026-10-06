# Se puede escoger donde sava insertar
li = [2, "a", 4]
li.insert(3, "c")

print(li)  # [2, 'a', 4, 'c']

# si esta en un numero que no existe lo se va al final
li = [2, "a", 4]
li.insert(12, "c")

print(li)  # [2, 'a', 4, 'c']

# si es sero o pone al principio
li = [2, "a", 4]
li.insert(0, "c")

print(li)  # [2, 'a', 4, 'c']