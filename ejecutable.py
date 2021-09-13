from clase_maquina_tragamonedas import maquina # esto es un comentario de prueba para Git

saldo_jugador=int(input("Ingrese su saldo inicial:"))
jugador_1=maquina(saldo_jugador)

while True:
    jugador_1.jugar()
    if jugador_1.saldo<=0:
        break
    else:
        input("Presione enter para continuar jugando:")
        jugador_1.jugar()

