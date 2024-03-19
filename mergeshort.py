import random
import time

def merge_sort(arr):
    # Esta función implementa el algoritmo de ordenamiento Mergesort.
    # Divide el arreglo en mitades, ordena cada mitad y luego fusiona las mitades ordenadas.

    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio del arreglo
        L = arr[:mid]  # Mitad izquierda
        R = arr[mid:]  # Mitad derecha

        # Llamada recursiva para ordenar la mitad izquierda
        merge_sort(L)
        # Llamada recursiva para ordenar la mitad derecha
        merge_sort(R)

        # Inicialización de variables para mezclar las dos mitades
        i = j = k = 0

        # Mezcla las dos mitades ordenadas
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Verifica si hay elementos restantes en la mitad izquierda
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Verifica si hay elementos restantes en la mitad derecha
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Solicita al usuario el tamaño del arreglo
n = int(input("Ingrese el tamaño del arreglo: "))

# Genera un arreglo aleatorio de tamaño n
arr = [random.randint(1, 1000) for _ in range(n)]
print("\nOriginal Array:", arr)

# Iniciamos el temporizador
start_time = time.time()

# Llamamos al algoritmo de ordenamiento Mergesort
merge_sort(arr)

# Calculamos el tiempo de ejecucion
end_time = time.time() - start_time

print("\nArreglo ordenado con Mergesort:", arr)
print("\nTiempo de ejecución:", end_time, "segundos")

