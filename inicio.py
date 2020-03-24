playlist={} #diccionario vacio
playlist['canciones']= []

#funcion principal
def app():

    #Agregar playlist
    agregar_playlist=True
    while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar la playlist?\r\n')
    
        if nombre_playlist:
            playlist['nombre']= nombre_playlist
            agregar_playlist=False
            agregarCanciones()


def agregarCanciones():
    agregarCancion = True

    while agregarCancion:
        nombre_playlist = playlist['nombre']
        pregunta = f'Agrega canciones para la playList {nombre_playlist}: \r\n'
        pregunta += 'Escribir "X" para dejar de agregar canciones \r\n'
    
        cancion= input(pregunta)

        if cancion =='X':
            print('finalizando...')
        else:
            playlist['canciones'].append(cancion)
            print(playlist)
        

app()