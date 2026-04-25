"""
EJERCICIO 8: 
"""

import random

class Personaje:
    def __init__(self):
        self.vidas=5
    
    def golpear(self):
        if self==jugador:
            sistema.vidas-=1
        else:
            jugador.vidas-=1
    
    def derribar(self):
        if self==jugador:
            sistema.vidas-=2
        else:
            jugador.vidas-=2

    def curarse(self):
        self.vidas+=2
    

jugador=Personaje()
sistema=Personaje()

while jugador.vidas>0 and sistema.vidas>0:
    print("Es tu turno, elige una de las opciones:")
    print("\n1- Golpear")
    print("2- Derribar")
    print("3- Curarse")
    op= int(input("Ingrese: "))

    if op==1:
        jugador.golpear()
    elif op==2:
        jugador.derribar()
    elif op==3:
        jugador.curarse()

    print(f"\nEl sistema tiene {sistema.vidas} vidas")
    print(f"Tu tienes {jugador.vidas} vidas")

    if sistema.vidas > 0:
        danio=random.randint(1,3)
        if danio==1:
            sistema.golpear()
            print("El sistema te ha golpeado")
        elif danio==2:
            sistema.derribar()
            print("El sistema te ha derribado")
        elif danio==3:
            sistema.curarse()
            print("El sistema se ha curado")

    print(f"\nEl sistema tiene {sistema.vidas} vidas")
    print(f"Tu tienes {jugador.vidas} vidas")

if jugador.vidas > 0:
    print("¡FELICITACIONES! Ganaste el duelo.")
else:
    print("GAME OVER. El sistema te ha derrotado.")
