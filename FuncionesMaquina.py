import random
class maquina(object):
    def __init__(self,saldo):
        self.saldo=saldo
 def jugar(self):
        simbolos=['$','@','&','#','7','%','!']
        simbolos_juego=list()
        for i in range(3):
            aleatorio=random.randint(0,6)
            simbolos_juego.append(simbolos[aleatorio])
        print(f"|{simbolos_juego[0]}||{simbolos_juego[1]}||{simbolos_juego[2]}|")
        self.validar(jugada=simbolos_juego)
        print(f"\nSu saldo es:{self.saldo}")
        
        
