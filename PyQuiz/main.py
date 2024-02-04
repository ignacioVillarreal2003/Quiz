from unidecode import unidecode
import random

diccionario_paises = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá',
    'México': 'Ciudad de México',
    'Estados Unidos': 'Washington DC',
    'Canadá': 'Ottawa',
    'Perú': 'Lima',
    'Venezuela': 'Caracas',
    'Ecuador': 'Quito',
    'España': 'Madrid',
    'Francia': 'París',
    'Italia': 'Roma',
    'Alemania': 'Berlín',
    'Reino Unido': 'Londres',
    'Rusia': 'Moscú',
    'China': 'Pekín',
    'Japón': 'Tokio',
    'Grecia': 'Atenas',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asunción',
    'Bolivia': 'La Paz',
    'Guatemala': 'Ciudad de Guatemala',
    'El Salvador': 'San Salvador',
    'Costa Rica': 'San José',
    'Panamá': 'Ciudad de Panamá',
    'Cuba': 'La Habana',
    'República Dominicana': 'Santo Domingo',
    'Puerto Rico': 'San Juan',
    'Haití': 'Puerto Príncipe'
}

diccionario_matematicas = {
    '¿Cuánto es 5 + 7?': 12,
    '¿Cuánto es 8 * 4?': 32,
    '¿Cuánto es 15 / 3?': 5,
    '¿Cuánto es 10 - 6?': 4,
    '¿Cuánto es 2 ** 3?': 8,
    '¿Cuánto es la raíz cuadrada de 25?': 5,
    '¿Cuánto es 9 % 4?': 1,
    '¿Cuánto es 3 + 4 * 2?': 11,
    '¿Cuánto es (6 + 2) / 2?': 4,
    '¿Cuánto es 10 // 3?': 3,
    '¿Cuánto es 7 ** 2?': 49,
    '¿Cuánto es 18 % 5?': 3,
    '¿Cuánto es la raíz cuadrada de 16?': 4,
    '¿Cuánto es 2 + 2 * 3?': 8,
    '¿Cuánto es (5 + 3) ** 2?': 64,
    '¿Cuánto es 20 // 7?': 2,
    '¿Cuánto es 13 % 5?': 3,
    '¿Cuánto es 9 - 2 * 3?': 3,
    '¿Cuánto es 4 ** 3?': 64,
    '¿Cuánto es la raíz cuadrada de 81?': 9,
    '¿Cuánto es 11 // 2?': 5,
    '¿Cuánto es 14 % 4?': 2,
    '¿Cuánto es 7 * 5 + 3?': 38,
    '¿Cuánto es (10 + 2) / 2?': 6,
    '¿Cuánto es 3 ** 4?': 81
}



def juegoPaises():
    print('Bienvenido a ¿Cual es la capital?')
    puntuacion = 0
    preguntas = 0
    print('--------------------------------------------------------------')
    accion = input('Ingrese JUGAR para jugar, ingrese SALIR para salir en cualquier momento: ').lower()
    print('--------------------------------------------------------------')

    listaDesordenada = []
    for e in diccionario_paises.keys():
        listaDesordenada.append(e)
    random.shuffle(listaDesordenada)

    if (accion == "jugar"):
        for e in listaDesordenada:
            print('---------------------')
            respuesta = input(f'¿Cual es la capital de {e}? ')
            print('---------------------')
            respuesta = unidecode(respuesta)
            respuesta = respuesta.lower()
            if (respuesta == "salir"):
                break
            elif (respuesta == unidecode(diccionario_paises[e]).lower()):
                puntuacion += 1
                print('Correcto.')
            else:
                print(f'Incorrecto, la capital es {diccionario_paises[e]}.')
            preguntas += 1
        print('Fin del juego.')
        print(f'Puntuacion: {puntuacion}/{preguntas}\n')
    elif (accion == "salir"):
        return
    else:
        print('Comando invalido.')
        juegoPaises()

def juegoMatematicas():
    print('Bienvenido a ¿Cual es el resultado?')
    puntuacion = 0
    preguntas = 0
    print('--------------------------------------------------------------')
    accion = input('Ingrese JUGAR para jugar, ingrese SALIR para salir en cualquier momento: ').lower()
    print('--------------------------------------------------------------')

    listaDesordenada = []
    for e in diccionario_matematicas.keys():
        listaDesordenada.append(e)
    random.shuffle(listaDesordenada)

    if (accion == "jugar"):
        for e in listaDesordenada:
            print('---------------------')
            respuesta = input(f'{e} ')
            print('---------------------')
            if (respuesta == "salir"):
                break
            elif (int(respuesta) == diccionario_matematicas[e]):
                puntuacion += 1
                print('Correcto.')
            else:
                print(f'Incorrecto, el resultado es {diccionario_matematicas[e]}.')
            preguntas += 1
        print('Fin del juego.')
        print(f'Puntuacion: {puntuacion}/{preguntas}\n')
    elif (accion == "salir"):
        return
    else:
        print('Comando invalido.')
        juegoPaises()


def main():
    comando = input('Ingrese 1 para jugar por capitales o 2 por matematica: ')
    if (comando == "1"):
        juegoPaises()
        main()
    elif (comando == "2"):
        juegoMatematicas()
        main()
    else:
        main()

if __name__ == '__main__':
    main()






