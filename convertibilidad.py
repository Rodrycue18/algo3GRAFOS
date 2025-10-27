transformacion = []
def esConv(x,y):

    global transformacion

    if (x <= y):
        # print("La cadena de transformacion es: ", x)
        transformacion.append(x)
    
    if x > y: 
        return False
    if x ==y:
        return True
    
    return esConv(x*2,y) or esConv((x*10) + 1 , y)

# print(esConv(1,82))
# print(contadorDellamados)
# print(transformacion)

# print(esConv(2,45))

def problema():
    global contadorDellamados
    global transformacion
    
    # Reinicializar variables globales
    contadorDellamados = 0
    transformacion = []
    
    x, y = map(int, input().split())
    res = esConv(x,y)
    trans = ""
    if res :
        print("YES")
        print(len(transformacion))
        for i in range(0,len(transformacion)-1):
            trans = trans + str(transformacion[i]) + " "
        trans = trans + str(transformacion[len(transformacion)-1])
        print(trans)
    else:
        print("NO")

problema()

def esConv(x, y, path):
    if x > y:
        return False
    
    path.append(x)
    
    if x == y:
        return True
    
    # Intentar primera operación: multiplicar por 2
    if esConv(x * 2, y, path):
        return True
    
    # Intentar segunda operación: x*10 + 1
    if esConv(x * 10 + 1, y, path):
        return True
    
    # Si ninguna funcionó, quitar x del path (backtrack)
    path.pop()
    return False