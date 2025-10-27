import sys

def alfabeticamente():
    INF = float('inf')

    # el input es muy raro, pero bueno
    n = int(sys.stdin.readline())
    costos = list(map(int, sys.stdin.readline().split()))
    strings = [sys.stdin.readline().strip() for _ in range(n)]

    # casos base
    costoNoFlipeadoPrevio = 0
    costoFlipeadoPrevio = costos[0]
    
    for i in range(1, n):
        # volteamos el string actual y el anterior
        stringActual = strings[i]
        stringflipeadoActual = stringActual[::-1]
        
        stringPrevio = strings[i-1]
        stringFlipeadoPrevio = stringPrevio[::-1]

        # Inicializar los costos del paso actual
        costoNoflipeadoActual = INF
        costoFlipeadoActual = INF

        
        if stringPrevio <= stringActual:
            costoNoflipeadoActual = min(costoNoflipeadoActual, costoNoFlipeadoPrevio)
        if stringFlipeadoPrevio <= stringActual:
            costoNoflipeadoActual = min(costoNoflipeadoActual, costoFlipeadoPrevio)

        
        if stringPrevio <= stringflipeadoActual:
            costoFlipeadoActual = min(costoFlipeadoActual, costoNoFlipeadoPrevio + costos[i])
        if stringFlipeadoPrevio <= stringflipeadoActual:
            costoFlipeadoActual = min(costoFlipeadoActual, costoFlipeadoPrevio + costos[i])
        
        
        costoNoFlipeadoPrevio = costoNoflipeadoActual
        costoFlipeadoPrevio = costoFlipeadoActual

    #el res
    result = min(costoNoFlipeadoPrevio, costoFlipeadoPrevio)

    if result == INF:
        print(-1)
    else:
        print(result)

alfabeticamente()