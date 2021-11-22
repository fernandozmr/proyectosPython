import random


def jugar():
    usuario = input ("Escoge una opcion: 'pi' para piedra, 'pa' para papel o 'ti' para tijera. \nYO: ").lower()
    computadora = random.choice (['pi', 'pa', 'ti'])
    print (f"COMPUTADORA: {computadora}")
#    print (gano_el_jugador(usuario,computadora)) #para control

    if usuario == computadora:
        return 'Empate!'

    if gano_el_jugador (usuario, computadora):
       return 'Ganaste!'


    return 'Perdiste!'

def gano_el_jugador (jugador, oponente):
        if ((jugador == 'pi' and oponente == 'ti') or (jugador == 'pa' and oponente == 'pi') or (jugador == 'ti' and oponente == 'pa')):
            return True
        else:
            False

print (jugar())
