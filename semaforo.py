import threading
import time

# semáforo con un contador inicial de 3
semaphore = threading.Semaphore(3)

# Función que simula el acceso a un recurso compartido
def acceso_al_recurso(identificador):
    print(f"Hilo {identificador} está esperando para acceder al recurso.")
    
    # Adquirir el semáforo
    semaphore.acquire()
    
    print(f"Hilo {identificador} ha obtenido acceso al recurso.")
    
    # Simular el uso del recurso compartido
    time.sleep(2)
    
    print(f"Hilo {identificador} ha terminado de usar el recurso.")
    
    # Liberar el semáforo
    semaphore.release()
    print(f"Hilo {identificador} ha liberado el recurso.")

# varios hilos que intentarán acceder al recurso compartido
hilos = []
for i in range(5):
    hilo = threading.Thread(target=acceso_al_recurso, args=(i,))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Todos los hilos han terminado.")