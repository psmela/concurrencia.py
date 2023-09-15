import threading

NUM_FILOSOFOS = 5

tenedores = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)]

def filosofo(filosofo_id):
    while True:
        tenedor_izq = tenedores[filosofo_id]
        tenedor_der = tenedores[(filosofo_id + 1) % NUM_FILOSOFOS]
        with tenedor_izq, tenedor_der:
            print(f"Filósofo {filosofo_id} está comiendo.")
            print(f"Filósofo {filosofo_id} ha terminado de comer.")

for i in range(NUM_FILOSOFOS):
    threading.Thread(target=filosofo, args=(i,)).start()