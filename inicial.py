from distancia import Distancia
import time

distancia = Distancia()
distancia.start()

while True:
    print( distancia.distancia )
    time.sleep(0.2)