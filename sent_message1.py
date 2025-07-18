<<<<<<< HEAD

sent_message = 'Hola mundo Este soy yo'

# Escribir el mensaje original en el archivo
with open('sent_message', 'w') as file:
    file.write(sent_message)

# Leer el mensaje original y modificar el archivo en el mismo bloque
with open('sent_message', 'r+') as file:  # r+ permite leer y escribir sin truncar
    # Leer el mensaje original
    original_message = file.read()
    
    # Mover el cursor al inicio o donde quieras escribir
    file.seek(0)
    
    # Mensaje modificado
    unsent_message = 'Este mensaje no ha sido enviado.'
    
    # Truncar el archivo al nuevo tamaño
    file.truncate(len(unsent_message))
    
    # Escribir el mensaje modificado
    file.write(unsent_message)

# Mostrar los mensajes
print('Original Message:', original_message)
=======

sent_message = 'Hola mundo Este soy yo'

# Escribir el mensaje original en el archivo
with open('sent_message', 'w') as file:
    file.write(sent_message)

# Leer el mensaje original y modificar el archivo en el mismo bloque
with open('sent_message', 'r+') as file:  # r+ permite leer y escribir sin truncar
    # Leer el mensaje original
    original_message = file.read()
    
    # Mover el cursor al inicio o donde quieras escribir
    file.seek(0)
    
    # Mensaje modificado
    unsent_message = 'Este mensaje no ha sido enviado.'
    
    # Truncar el archivo al nuevo tamaño
    file.truncate(len(unsent_message))
    
    # Escribir el mensaje modificado
    file.write(unsent_message)

# Mostrar los mensajes
print('Original Message:', original_message)
>>>>>>> 578aa10 (Primer commit)
print('Unsent Message:', unsent_message)