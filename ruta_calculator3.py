import heapq
import random

# Definición de matriz del mapa con una lista de ceros, donde los ceros representan caminos o espacios
mapa = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Funciones para encontrar la ruta mas corta
def encontrar_ruta(mapa, inicio, fin): #Esta funcion recibe el mapa, y las coordenadas de inicio y fin, y devuelve  una lista con las coordenadas de la ruta mas corta entre 2 puntos.
    direccion = [(-1, 0), (1, 0), (0, -1), (0, 1)] #Definicion de las direcciones (arriba, abajo, izquierda, derecha) 
    num_filas = len(mapa)
    num_columnas = len(mapa[0])
    
    def heuristica(pos_actual, pos_final): #Funcion Heuristica 
        return abs(pos_actual[0] - pos_final[0]) + abs(pos_actual[1] - pos_final[1])
    
    #Definimos las variables
    heap = [(0, inicio)]
    heapq.heapify(heap)
    padres = {inicio: None}
    costos = {inicio: 0}
    
    while heap:
        costo_actual, nodo_actual = heapq.heappop(heap)
        
        if nodo_actual == fin:
            break
        
        for direccion in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vecino = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            
            if 0 <= vecino[0] < num_filas and 0 <= vecino[1] < num_columnas:
                nuevo_costo = costo_actual + 1
                
                if mapa[vecino[0]][vecino[1]] != 1 and (vecino not in costos or nuevo_costo < costos[vecino]):
                    costos[vecino] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(vecino, fin)
                    heapq.heappush(heap, (prioridad, vecino))
                    padres[vecino] = nodo_actual 
    ruta = []
    nodo = fin
    while nodo is not None:
        ruta.append(nodo)
        nodo = padres[nodo]
    ruta.reverse()
    
    return ruta

def mostrar_mapa_con_ruta(mapa, ruta):
    num_filas = len(mapa)
    num_columnas = len(mapa[0])
    
    print('   ', end='')
    for col in range(num_columnas):
        print(f'{col:2}', end=' ')
    print()
    
    for fila in range(num_filas):
        print(f'{fila:2} ', end='')
        
        for col in range(num_columnas):
            if mapa[fila][col] == 0:
                if (fila, col) in ruta:
                    print('\033[1;32m* \033[0m', end='')  # Ruta o camino recorrido en verde
                else:
                    print('. ', end='')  
            else:
                print('\033[1;31m# \033[0m', end='')  # Obstáculos en rojo
        print()

def agregar_obstaculos(mapa, obstaculos):
    for obstaculo in obstaculos:
        if 0 <= obstaculo[0] < len(mapa) and 0 <= obstaculo[1] < len(mapa[0]):
            mapa[obstaculo[0]][obstaculo[1]] = 1
    return mapa

def coordenadas_validas(mapa, coordenadas):
    return (0 <= coordenadas[0] < len(mapa) and 
            0 <= coordenadas[1] < len(mapa[0]) and 
            mapa[coordenadas[0]][coordenadas[1]] == 0)

def generar_obstaculos_aleatorios(mapa, num_obstaculos):
    obstaculos = set()
    while len(obstaculos) < num_obstaculos:
        x = random.randint(0, len(mapa) - 1)
        y = random.randint(0, len(mapa[0]) - 1)
        if mapa[x][y] == 0:
            obstaculos.add((x, y))
    return list(obstaculos)

if __name__ == "__main__":
    num_filas = len(mapa)
    num_columnas = len(mapa[0])
    
    print("Mapa inicial:")
    print('   ', end='')
    for col in range(num_columnas):
        print(f'{col:2}', end=' ')
    print()
    
    for fila in range(num_filas):
        print(f'{fila:2} ', end='')
        for col in range(num_columnas):
            if mapa[fila][col] == 0:
                print('. ', end='')  
            else:
                print('# ', end='')  
        print()
    
    modo = input("Selecciona modo de ingreso de obstáculos (1: manual, 2: aleatorio): ")
    
    if modo == '1':
        obstaculos = []
        while True:
            entrada = input("Ingresa coordenadas de un obstáculo (formato x,y) o 'fin' para terminar: ")
            if entrada.lower() == 'fin':
                break
            x, y = map(int, entrada.split(','))
            obstaculos.append((x, y))
    elif modo == '2':
        num_obstaculos = int(input("Ingresa el número de obstáculos aleatorios: "))
        obstaculos = generar_obstaculos_aleatorios(mapa, num_obstaculos)
    
    mapa = agregar_obstaculos(mapa, obstaculos)
    
    print("\nMapa con obstáculos:")
    mostrar_mapa_con_ruta(mapa, [])
    
    while True:
        inicio = tuple(map(int, input("Ingresa coordenadas de inicio (formato x,y): ").split(',')))
        if coordenadas_validas(mapa, inicio):
            break
        print("Coordenadas no válidas o es un obstáculo. Intenta de nuevo.")
    
    while True:
        fin = tuple(map(int, input("Ingresa coordenadas de destino (formato x,y): ").split(',')))
        if coordenadas_validas(mapa, fin):
            break
        print("Coordenadas no válidas o es un obstáculo. Intenta de nuevo.")
    
    ruta_encontrada = encontrar_ruta(mapa, inicio, fin)
    
    print("\nMapa con ruta más corta:")
    mostrar_mapa_con_ruta(mapa, ruta_encontrada)
