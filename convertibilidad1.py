
def esConv(x, y, transformacion):
    if x > y:
        return False
    
    transformacion.append(x)
    
    if x == y:
        return True
    
    if esConv(x * 2, y, transformacion):
        return True
    
    if esConv(x * 10 + 1, y, transformacion):
        return True
    
    transformacion.pop()
    return False

# print(esConv(1,82))
# print(contadorDellamados)
# print(transformacion)

# print(esConv(2,45))

def problema():

    global transformacion
    transformacion = []
    contadorDellamados = 0
    #manera rara del input para codeforces
    x, y = map(int, input().split())
    res = esConv(x,y,transformacion)
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