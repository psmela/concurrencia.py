import threading

NUM_LECTORES = 3
NUM_ESCRITORES = 2

lector_mutex = threading.Semaphore(1)
escritor_mutex = threading.Semaphore(1)
leyendo = 0

def lector():
    global leyendo
    while True:
        with lector_mutex:
            leyendo += 1
            if leyendo == 1:
                escritor_mutex.acquire()
        print("Leyendo...")
        with lector_mutex:
            leyendo -= 1
            if leyendo == 0:
                escritor_mutex.release()

def escritor():
    while True:
        with escritor_mutex:
            print("Escribiendo...")

for _ in range(NUM_LECTORES):
    threading.Thread(target=lector).start()

for _ in range(NUM_ESCRITORES):
    threading.Thread(target=escritor).start()







