import numpy as np
import time

n = 1000000

# Método Python tradicional
start = time.time()
lista = []
for i in range(n):
    lista.append(i * 2)
tiempo_append = time.time() - start

# Método Python pre-dimensionado
start = time.time()
lista = [None] * n
for i in range(n):
    lista[i] = i * 2
tiempo_predim = time.time() - start

# Método NumPy - RESERVAR MEMORIA + INDEXAR
start = time.time()
arr = np.empty(n, dtype=np.int64)  # Reserva memoria sin inicializar
for i in range(n):
    arr[i] = i * 2
tiempo_numpy_manual = time.time() - start

# Método NumPy - VECTORIZADO (EL MÁS RÁPIDO)
start = time.time()
arr = np.arange(n) * 2
tiempo_numpy_vec = time.time() - start

print(f"Append Python:      {tiempo_append:.4f}s")
print(f"Pre-dim Python:     {tiempo_predim:.4f}s") 
print(f"NumPy manual:       {tiempo_numpy_manual:.4f}s")
print(f"NumPy vectorizado:  {tiempo_numpy_vec:.4f}s")
print(f"\nMejoras vs append:")
print(f"NumPy manual:    {tiempo_append/tiempo_numpy_manual:.0f}x más rápido")
print(f"NumPy vectorizado: {tiempo_append/tiempo_numpy_vec:.0f}x más rápido")