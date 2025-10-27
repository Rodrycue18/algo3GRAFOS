#paso en limpio el ejercicio A , corrigiendo la cola
from collections import deque

def maquina(n ,m):
    #genero mi grafo con n como raiz
    grafo = {}
    grafo[(n,0)] = []
    m = (m,-1)
    raiz = list(grafo.keys())
    def bfs(graph,node,m):
        visited = []
        queue = deque()

        visited.append(node)
        queue.append(node)
        
        while queue:
            #Esta parte esta al pepe
            # rojo = (-1,-1)
            # azul = (-1,-1)

            s = queue.popleft()
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