import random
import time

def ternary_search(arr, left, right, x):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Si el elemento esta presente en uno de los tercios
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        # Si el elemento es menor que el elemento en el primer tercio, busca en la primera parte
        if arr[mid1] > x:
            return ternary_search(arr, left, mid1 - 1, x)

        # Si el elemento es mayor que el elemento en el tercer tercio, busca en la tercera parte
        elif arr[mid2] < x:
            return ternary_search(arr, mid2 + 1, right, x)

        # Si el elemento esta entre el primer y tercer tercio, busca en la segunda parte
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)

    # Si el elemento no esta presente en el arreglo
    return -1

# Solicitamos al usuario el tamaño del arreglo
n = int(input("Ingrese el tamaño del arreglo: "))

# Generamos un arreglo aleatorio de tamaño n
arr = [random.randint(1, 1000) for _ in range(n)]
arr.sort()  # Ordena el arreglo, ya que la búsqueda ternaria requiere que el arreglo esté ordenado

x = 15  # Elemento a buscar

# Iniciamos temporizador
start_time = time.time()

result = ternary_search(arr, 0, n - 1, x)

# Calculamos el tiempo de ejecucion
end_time = time.time() - start_time

print("\nArreglo creado:", arr)

if result != -1:
    print(f"\nEl elemento {x} está presente en el índice {result}")
else:
    print("\nEl elemento no está presente en el arreglo")

print("\nTiempo de ejecución:", end_time, "segundos")