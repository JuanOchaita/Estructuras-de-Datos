import cProfile
import pstats
import io
import time

from memory_profiler import profile

start = time.time()

@profile
def suma_lista(lista):
    suma = 0  # O(1) - espacio constante
    for num in lista:  # O(1) - no se usa espacio adicional por iteración
        suma += num
    return suma

@profile
def run_profiled_hello_world():

    numeros = [2,3,5]

    pr = cProfile.Profile()
    pr.enable()
    suma_lista(numeros)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

    end = time.time()

    print(f"Tiempo de ejecución: {end - start:.6f} segundos")

if __name__ == "__main__":
    run_profiled_hello_world()
