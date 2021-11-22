import random #importa un modulo
import string
from palabras import palabras # importa un elemento del modulo
from vidas_diccionario_visual import vidas_diccionario_visual

def obtener_palabra_valida (lista_palabras):
    palabra = random.choice (lista_palabras)
    return palabra

    while '_' in palabra or ' ' in lista_palabras:
        palabra =  random.choice(lista_palabras)

    return palabra.upper()

def ahorcado():

    print ("========================================")
    print ("Bienvenide al juego del ahorcado")
    print ("========================================")

    palabra = obtener_palabra_valida (palabras).upper()

    letras_por_adivinar = set(palabra) #conjunto --> es como una lista pero NO puede haber elementos repetidos
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras : {' '.join(letras_adivinadas)} ")

        palabra_lista = [letra if letra in letras_adivinadas
                            else '-' for letra in palabra] #Para cada letra de la Palabra (palabra seleccionada por la maquina) y que en letras_adivinadas inluyela en la palabra_lista sino incluye '-'
    
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -=1
                print(f"\nTu letra {letra_usuario} no esta en la palabra. ")    

        elif letra_usuario in letras_adivinadas: 
            print("\nYa has escogido esta letra, por favor elige otra letra")
        
        else:
            print("\Esta letra NO es valida")


    #El juego llega esta linea cuando se adivinan todas las letras de la palabra o se quedo sin vidas 
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado! Has perdido. La palabra era: {palabra}")

    else:
        print (f"Ganaste!. Adivinaste la palabra {palabra}")   


ahorcado()