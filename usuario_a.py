def fibonacci(n):
    if n <= 0:
        print("Error: el número debe ser mayor que 0")
        return

    a, b = 0, 1
    serie = []

    for _ in range(n):
        serie.append(a)
        a, b = b, a + b

    print("Serie Fibonacci:", " ".join(map(str, serie)))