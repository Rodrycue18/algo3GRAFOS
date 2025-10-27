# t = int(input())   # cantidad de casos
# i = 1

# for _ in range(t):
#     n = int(input())   # longitud (no siempre necesaria)
#     s = input().strip()
#     # acá ya tenés n y s para cada test
#     print(f"el input nro {i}, tiene longitud {n} y es el string {s}")
#     i = i+1


# print("el t es " + str(t))

def problema():
    n = int(input())
    s = input().strip()
    ans = lLindo(s, caracter = 'a')
    print(ans)

def lLindo(s,caracter):
    n = len(s)
    if n == 1:
        if s[0] ==  caracter:
            return 0
        else:
            return 1

    mitad = n//2
    izquierda = s[:mitad]
    derecha = s[mitad:]
    cambiosIzq = contador(izquierda, caracter)
    costo1 = cambiosIzq + lLindo (derecha,sigt(caracter))

    cambiosDer = contador(derecha,caracter)
    costo2 = cambiosDer + lLindo(izquierda ,sigt(caracter))

    return min(costo1,costo2)

def contador(lista,caracter):
    cont= 0
    for i in lista:
        if i != caracter:
            cont = cont +1
    
    return cont

def sigt (caracter):
    posicion = ord(caracter)+1
    return chr(posicion)

t = int(input())
for _ in range(t):
    problema()

