import random
import time

def simular_infeccion(n):
    # Creamos una lista de nodos, donde inicialmente todos están sanos (0) excepto uno infectado (1)
    nodos = [0] * n
    nodo_infectado = random.randint(0, n-1)
    nodos[nodo_infectado] = 1
    return nodos, nodo_infectado

def pull(nodos):
    # Enfoque pull: un nodo infectado intenta infectar a sus nodos vecinos
    for i in range(len(nodos)):
        if nodos[i] == 1:
            for j in range(max(0, i-1), min(len(nodos), i+2)):
                if nodos[j] == 0 and random.random() < 0.5:
                    nodos[j] = 1
    return nodos

def push(nodos):
    # Enfoque push: un nodo sano es infectado por un nodo infectado vecino
    for i in range(len(nodos)):
        if nodos[i] == 1:
            for j in range(max(0, i-1), min(len(nodos), i+2)):
                if nodos[j] == 0 and random.random() < 0.5:
                    nodos[j] = 1
                    if j in nodos_no_infectados:  # Verificar si el nodo no está ya infectado
                        nodos_no_infectados.remove(j)
                    return j  # Devolver el índice del nodo infectado

def pull_push(nodos):
    # Enfoque pull-push: combina el pull y el push
    for i in range(len(nodos)):
        if nodos[i] == 1:
            for j in range(max(0, i-1), min(len(nodos), i+2)):
                if nodos[j] == 0 and random.random() < 0.5:
                    nodos[j] = 1
    for i in range(len(nodos)):
        if nodos[i] == 1:
            for j in range(max(0, i-1), min(len(nodos), i+2)):
                if nodos[j] == 0 and random.random() < 0.5:
                    nodos[j] = 1
                    if j in nodos_no_infectados:  # Verificar si el nodo no está ya infectado
                        nodos_no_infectados.remove(j)
                    return j  # Devolver el índice del nodo infectado

# Simulación inicial
n = 10
nodos, nodo_infectado_inicialmente = simular_infeccion(n)
tiempo_inicio = time.time()

# Lista para registrar el estado de cada nodo en cada iteración
estado_nodos = []

# Lista para registrar los nodos infectados, no infectados y suspendidos
nodos_infectados = [nodo_infectado_inicialmente]
nodos_no_infectados = list(range(n))
nodos_no_infectados.remove(nodo_infectado_inicialmente)
nodos_suspendidos = []

# Inicializar el tiempo de duración de la infección
duracion_infeccion = 0

while duracion_infeccion < 5:  # Simular durante 10 segundos
    tiempo_actual = time.time()
    duracion_infeccion = tiempo_actual - tiempo_inicio
    
    # Pull
    nodos_pull = pull(nodos[:])
    estado_nodos.append(nodos_pull[:])
    
    # Push
    nodo_infectado_push = push(nodos[:])
    if nodo_infectado_push is not None:
        nodos_infectados.append(nodo_infectado_push)
        if nodo_infectado_push in nodos_no_infectados:  # Verificar si el nodo no está ya infectado
            nodos_no_infectados.remove(nodo_infectado_push)
    
    # Pull-push
    nodo_infectado_pull_push = pull_push(nodos[:])
    if nodo_infectado_pull_push is not None:
        nodos_infectados.append(nodo_infectado_pull_push)
        if nodo_infectado_pull_push in nodos_no_infectados:  # Verificar si el nodo no está ya infectado
            nodos_no_infectados.remove(nodo_infectado_pull_push)
    
    # Actualizar la lista de nodos suspendidos
    nodos_suspendidos_temporal = [n for n in nodos_no_infectados if random.random() < 0.1]
    for nodo_suspendido in nodos_suspendidos_temporal:
        nodos_suspendidos.append(nodo_suspendido)
        nodos_no_infectados.remove(nodo_suspendido)
    
    # Mostrar el tiempo de duración de la infección
    print("Tiempo de duración de la infección: {:.2f} segundos".format(duracion_infeccion))
    
    # Mostrar los nodos infectados, no infectados y suspendidos
    print("Nodos infectados:", nodos_infectados)
    print("Nodos no infectados:", nodos_no_infectados)
    print("Nodos suspendidos:", nodos_suspendidos)
    
    # Esperar 1 segundo antes de la próxima iteración
    time.sleep(1)
    
    # Simular infectar a cinco computadoras adicionales
print("\nInfectando cinco computadoras adicionales:")

for _ in range(5):
    nodo_nuevo = random.randint(0, n-1)
    while nodo_nuevo in nodos_infectados:
        nodo_nuevo = random.randint(0, n-1)
    nodos_infectados.append(nodo_nuevo)
    if nodo_nuevo in nodos_no_infectados:  # Verificar si el nodo no está ya infectado
        nodos_no_infectados.remove(nodo_nuevo)
    
    print("Nueva computadora infectada:", nodo_nuevo)

