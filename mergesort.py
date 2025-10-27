import math
def merge(listaog,inicio,medio,final):
    #Saco tamanos de ambas sublista para llenarlas en izq y der
    mediobajo = medio-inicio+1
    medioarriba = final-medio
    izq=[0]* (mediobajo +1)
    der=[0]* (medioarriba +1)
    for i in range(mediobajo):
        # izq.append(listaog[inicio+i])
         izq[i] = listaog[inicio + i]
    
    for j in range(medioarriba):
        # der.append(listaog[medio+j+1])
        der[i] = listaog[medio + j+1]
    
    # print("la lista izq" + str(izq))
    # print ("la lista der" +str(der))
    
    # izq.append(None)
    # der.append(None) #chequear que las pilas esten vacias
    izq[mediobajo] = math.inf
    der[medioarriba] = math.inf

    i = 0
    j = 0
    k = inicio
    for k in range(final):
        # print (f"{listaog} y el i = {i} , j = {j}")
        if izq[i] <= der[j]:
            listaog[k] = izq[i]
          
            i = i+1

        else:
            listaog[k] = der[j]
            
            j = j+1
            
    # print (listaog)

# merge([2,3,5,0,1,4,19,11],0,3,7)
# izq = [2,3,5,6] der = [1,4,11,19]

def mergesort(listaog,inicio,final):
    if inicio<final:
        medio = math.floor((inicio+final)/2)
        mergesort(listaog,inicio,medio)
        mergesort(listaog,medio+1,final)
        merge(listaog,inicio,medio,final)


listaog = [4,5,8,2,1,7,33,12]

mergesort(listaog,0,7)
print(listaog)

