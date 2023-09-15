import threading
import time
import random
from queue import Queue

TAMANO_BUFFER = 5

buffer = Queue(maxsize=TAMANO_BUFFER)

def productor():
    while True:
        item = random.randint(1, 100)
        buffer.put(item)
        print(f"Productor produjo: {item}")
        time.sleep(random.uniform(0.1, 0.5))

def consumidor():
    while True:
        item = buffer.get()
        print(f"Consumidor consumió: {item}")
        buffer.task_done()
        time.sleep(random.uniform(0.1, 0.5))

# Crear hilos de productores y consumidores
hilos = [threading.Thread(target=productor) for _ in range(3)] + [threading.Thread(target=consumidor) for _ in range(2)]

# Iniciar hilos
for hilo in hilos:
    hilo.start()

# Esperar a que todos los hilos terminen (esto se ejecuta en un ciclo infinito)
for hilo in hilos:
    hilo.join()





