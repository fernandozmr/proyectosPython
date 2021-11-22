import random

def adivina_el_numero2 (x):
    print ("==================================================")
    print (f"Adivina el numero!. En esta oportunidad, pensaras un número entre 1 y {x}. Sera la maquina quien adivinara")
    print ("==================================================")
    print ("===========¡Empecemos!===============")
    print (f"Piensa un número entre 1 y {x}")
    
    num = random.randint(1,x)

    while true:
        print (f"La maquina dice que el numero que pensaste es {num} ! Estoy en lo correcto?")
        res = input ("Estoy en lo correcto (s), No, no es el número que pense (n)")
        if res == "n":
            print (f"OK, el numero que pensaste es mayor o menor a {num} ?")
            res2= input (Menor (m) / Mayor (M))
            if res2 == "M":
                num = random.randint(num+1,x)
            else: num = random.randint (1,num-1)   
        else: break

    print ("Genial, gracias por jugar conmigo")


adivina_el_numero2(10)
