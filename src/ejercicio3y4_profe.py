def imprime_pares(n):
    for i in range(2, n+1, 2):
        print(i, end = " ")
    
def imprime_pares_inverso(n):
    if n % 2 != 0: #si es impar...
        n -= 1
    for i in range(n, 1, -2):
        print(i, end = ' ')


imprime_pares(7)
imprime_pares_inverso(7)