
from functools import reduce


playlist = [('What Was I Made For?', 3.42), 
            ('Just Like That', 5.05), 
            ('Song 3', 6.8), 
            ('Leave The Door Open', 4.02), 
            ('I Can\'t Breath', 4.47), 
            ('Bad Guy', 3.14)] 


# Funcion filter
def longer_than_five_minutes(song):
    return song[1] > 5


# Fuincion Map 
def convert_song(song):
    duration = song[1]    # creramos variable duracion y le asignamos el segundo valod de la tupla "Con Decimales"
    minutes = int(duration)   # Creamos variable minutes y almacenamos la variable duracioin convirtiendola a numero entero "Sin decimales"
    seconds = (duration - minutes) * 100  # Creamos variable seconds 

    return minutes * 60 + round(seconds)


# funcion reduce 
def sumar_tiempo(total, song):
    duracion = song[1]
    return total + duracion


filtered_songs = list(filter(longer_than_five_minutes, playlist))

convert_to_seconds = list(map(convert_song, playlist))

total_playtime = reduce(sumar_tiempo, playlist, 0)


print(filtered_songs) 
print(convert_to_seconds)
print(total_playtime)