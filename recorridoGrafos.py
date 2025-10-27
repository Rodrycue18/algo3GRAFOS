from collections import deque
from typing import Dict,Tuple
def dfs(graph,node):
    visited = [] #lista de visitados
    stack = deque() #esto me ayuda para hacer backtrack a un nodo , se podria decir que sirve para iterar
    #inicializacion
    visited.append(node) #trivialote,el nodo padre es el primero en ser visitado
    stack.append(node) # de todas maneras lo agrego a la pila

    while stack: #While stack not empty , por eso agregamos el nodo raiz
        s = stack.pop() # saco el nodo que ya visite y s = 'A', s representa el nodo donde estoy parado
        print(s,end=" ")

        for n in reversed(graph[s]): #Caso con for n in reversed(graph['A']) -> for n in ['G','B']
            if n not in visited:
                visited.append(n)
                stack.append(n)


def bfs(graph,node):
    visited = []
    queue = []
    
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end=" ")
        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

graphdfs = {
    'A': ['B','G'],
    'B': ['C','D','E'],
    'C' : [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'], 
    'H': ['I'],
    'I': []
}

graphbfs = {
    'A': ['B','C'],
    'B': ['D','E','F'],
    'C' : ['G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': ['I'], 
    'H': [],
    'I': []
}

# dfs(graphdfs,'A')
# print("\n")
# bfs(graphbfs, 'A')

# print(type(graph))
# print(graph['A'])
# print(reversed(graph))
# printeo = []
# for k,v in graph.items():
#     printeo.append((k,v))

# print(printeo)

#--------
#Carlos ha encontrado un dispositivo extraño. En el panel frontal del dispositivo hay: un botón rojo,
# un botón azul y una pantalla que muestra un número entero positivo. Después de presionar el botón rojo,
#  el dispositivo multiplica el número mostrado por dos. Después de presionar el botón azul, 
# el dispositivo resta uno al número en la pantalla. Si en algún momento el número deja de ser positivo,
#  el dispositivo se descompone. La pantalla puede mostrar números arbitrariamente grandes. 
# Inicialmente, la pantalla muestra el número n , Ana quiere obtener el número m
#  en la pantalla. ¿Cuál es el número mínimo de clics que tiene que hacer para lograr este resultado?

# Input
# La primera y única línea de la entrada contiene dos enteros distintos n
#  y m (1≤n,m≤10^4), separados por un espacio.

# Output
# Imprima un solo número: el número mínimo de veces que se necesita presionar el botón requerido 
# para obtener el número m , a partir del número n
# Input : 8 12 -> Output:3

def maquina(n ,m):
    #genero mi grafo con n como raiz
    grafo = {}
    grafo[(n,0)] = []
    m = (m,-1)
    raiz = list(grafo.keys())
    def bfs(graph,node,m):
        visited = []
        queue = []

        visited.append(node)
        queue.append(node)
        
        while queue:
            #Esta parte esta al pepe
            # rojo = (-1,-1)
            # azul = (-1,-1)

            s = queue.pop(0)
            if s[0] == m[0]: #retorno nivel
                return s[1]
            # genero arbol 
            #Camino 1
            # rojo[0] = (graph[s][0]) * 2
            # rojo[0] = s[0] * 2
            # rojo[1] = s[1] + 1
            rojo = (s[0] * 2,s[1] + 1)
            #camino 
            # azul[0] = s[0] - 1
            # azul[1] = s[1] + 1
            azul = (s[0] - 1,s[1] + 1)
            #actualizo grafo con mis nuevos caminos
            graph[s] = [rojo,azul]

            # print(s) #Printeo nodo que saco de la cola
            for n in graph[s]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)

    return bfs(grafo,raiz[0],m)

# print(maquina(8,12))
# print(maquina(20,15))

def problemaA():
    x, y = map(int, input().split())
    print(maquina(x,y))


problemaA()
