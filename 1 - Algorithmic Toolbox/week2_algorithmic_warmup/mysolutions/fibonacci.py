# Uses python3
def calc_fib(n):
    lista = []
    lista.append(0)
    lista.append(1)
    if n <= 1:
        return n

    for i in range(2, n + 2):
        lista.append(lista[i-1] + lista[i-2])
    
    return lista[n]

n = int(input())
print(calc_fib(n))
