#METHODES PIVOT DE GAUSS#

def recherche_pivot(A, b, j):
    p = j
    for i in range(j+1, A.shape[0]):
        if abs(A[i, j]) > abs(A[p, j]):
            p = i
        if p != j :
            b[[p, j]] = b[[j, p]]
            A[[p, j]] = A[[j, p]]

def elimination_bas(A, b, j):
    for i in range(j+1, A.shape[0]):
        b[i] = b[i] - (A[i, j] / A[j, j]) * b[j]
        A[i] = A[i] - (A[i, j] / A[j, j]) * A[j]

def descente(A, b):
    for j in range(A.shape[1] -1) :
        recherche_pivot(A, b, j)
        elimination_bas(A, b, j)

def elimination_haut(A, b, j):
    for i in range(j):
        b[i] = b[i] - ((A[i, j] / A[j, j]) * b[j])

def remontee(A, b):
    for j in range(A.shape[1] - 1, 0, -1):
        elimination_haut(A, b, j)

def solve_diagonal(A, b):
    for k in range(b.shape[0]):
        b[k] = b[k] / A[k, k]
    return b

def gauss(A, b):
    U = A.copy()
    v = b.copy()
    descente(U, v)
    remontee(U, v)
    return solve_diagonal(U, v)




