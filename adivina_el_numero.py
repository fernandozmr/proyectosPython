import random

def adivina_el_numero(x): # x es el limite superior del rango del numero a adivinar

    print ("----------------Bienvenido man o mana------------------")
    print ("Tu meta es adivinar el numero generado por la computadora")

    num_aleatorio = random.randint(1,x) # número aleatorio entre 1 y x inclusive
    #print (f"(el numero que esta esta maquina es {num_aleatorio})")
    prediccion = 0

    while prediccion != num_aleatorio:
        #aqui el usuario ingresa un numero
        prediccion = int(input (f"Adivina un numero entre 1 y {x}: ")) #f - string

        if prediccion < num_aleatorio:
            print (f"Intenta otra vez. el {prediccion} es menor que el numero pensado por la maquina")
        elif prediccion > num_aleatorio:
            print (f"Intenta otra vez. el {prediccion} es mayor que el numero pensado por la maquina")


    print (f"Felicitaciones, {num_aleatorio} es el numero que penso esta maquina!!")


adivina_el_numero (10)