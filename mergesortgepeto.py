import math

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # Creamos arreglos L y R con un espacio extra para el "sentinel"
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Copiamos los elementos a L y R
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]

    # Sentinels (∞)
    L[n1] = math.inf
    R[n2] = math.inf

    i = 0
    j = 0

    # Merge
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)



a = [38, 27, 43, 3, 9, 82, 10]
print("Arreglo original:", a)
merge_sort(a, 0, len(a) - 1)
print("Arreglo ordenado:", a)
