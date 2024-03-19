import random
import time

def partition(arr, low, high):
    # Esta funcion implementa el paso de partición del algoritmo Quicksort.
    # Toma un arreglo arr y dos índices low y high para delimitar la porción del arreglo a considerar.
    # Devuelve el indice del pivote después de haberlo colocado en su posicion correcta en el arreglo.

    pivot = arr[high]  # Toma el ultimo elemento como el pivote
    i = low - 1  # Inicializa el indice del elemento mas pequeño

    # Recorre el arreglo desde low hasta high - 1
    for j in range(low, high):
        if arr[j] < pivot:
            # Si el elemento actual es menor que el pivote,
            # incrementa el indice del elemento más pequeño
            i += 1
            # Intercambia arr[i] y arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Intercambia arr[i+1] y arr[high] (o el pivote)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Devuelve el indice del pivote despues de la particion


def quick_sort(arr, low, high):
    # Esta funcion implementa el algoritmo Quicksort.
    # Toma un arreglo arr y dos indices low y high para delimitar la porcion del arreglo a considerar.

    if low < high:
        # Si low es menor que high, el arreglo tiene mas de un elemento
        # y el ordenamiento es necesario.

        pi = partition(arr, low, high)  # Encuentra la particion del arreglo

        # Llama recursivamente a quick_sort para las dos mitades del arreglo
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Solicitamos al usuario el tamaño del arreglo
n = int(input("Ingrese el tamaño del arreglo: "))

# Generamos el arreglo aleatorio de tamaño n
arr = [random.randint(1, 1000) for _ in range(n)]
print("\nOriginal Array:", arr)

# Iniciamos el temporizador
start_time = time.time()

# Llamamos al algoritmo de ordenamiento Quicksort
quick_sort(arr, 0, len(arr) - 1)

# Calculamos el tiempo de ejecución
end_time = time.time() - start_time

print("\nArreglo ordenado con Quicksort:", arr)
print("\nTiempo de ejecución:", end_time, "segundos")
