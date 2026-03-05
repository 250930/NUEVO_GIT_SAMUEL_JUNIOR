def fibonacci(n):
    
    if n <= 0:
        print("Ingrese un número mayor que 0")
        return

    a = 0
    b = 1
    contador = 0

    print("Serie Fibonacci:")

    while contador < n:
        print(a, end=" ")
        siguiente = a + b
        a = b
        b = siguiente
        contador += 1