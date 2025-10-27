
def permutacion(listadep,listadepog,lista = []):
    if lista == None:
        lista = []
    if len(listadep) == 0:
        return [[]]
    
    # if (len(lista) == len(listadepog)) and (len(listadep) == 0) :
    if (len(lista) == len(listadepog)) :
        return [lista]
    
    for i in range(0,len(listadep)):
        lista = []
        return [] + permutacion(listadep[1:],listadepog,lista.append(listadep[i]))

print(permutacion([1,2,3],[1,2,3],[]))