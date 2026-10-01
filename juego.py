#marvin joel avila galicia
"""
entrada: se usara nombre, vida etc como objeto y clase 
proceso: se mirara el daño, los niveles y los trofeos
salida: se pondra todo en orden si sale correcto
"""
import random
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
    def atacar(self, enemigo):
        daño = random.randint(1, self.ataque)
        enemigo.vida -= daño
        print(self.nombre, "hizo", daño, "de daño a", enemigo.nombre)
jugador = Personaje("Guerrero", 100, 20)
for nivel in range(1, 4):
    enemigo = Personaje("Enemigo", 30 + nivel * 10, 10)
    print("\nNivel", nivel)
    while jugador.vida > 0 and enemigo.vida > 0:
        jugador.atacar(enemigo)
        if enemigo.vida > 0:
            enemigo.atacar(jugador)
    if jugador.vida <= 0:
        print("Perdiste.")
        break
    print("¡Ganaste el nivel!")
if jugador.vida > 0:
    print("¡Ganaste el juego!")