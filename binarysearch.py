import random
import time

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Si el elemento está presente en el medio
        if arr[mid] == x:
            return mid

        # Si el elemento es mayor, ignora la mitad izquierda
        elif arr[mid] < x:
            left = mid + 1

        # Si el elemento es menor, ignora la mitad derecha
        else:
            right = mid - 1

    # Si el elemento no está presente en el arreglo
    return -1

# Solicitar al usuario el tamaño del arreglo
n = int(input("Ingrese el tamaño del arreglo: "))

# Generar arreglo aleatorio de tamaño n
arr = [random.randint(1, 1000) for _ in range(n)]
arr.sort()  # Ordena el arreglo, ya que la búsqueda binaria requiere que el arreglo esté ordenado

x = 10  # Elemento a buscar

# Iniciar temporizador
start_time = time.time()

result = binary_search(arr, x)

# Calcular el tiempo de ejecución
end_time = time.time() - start_time

print("\nArreglo creado:", arr)

if result != -1:
    print(f"\nEl elemento {x} está presente en el índice", result)
else:
    print("\nEl elemento no está presente en el arreglo")

print("\nTiempo de ejecución:", end_time, "segundos")
