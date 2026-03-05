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

def capicua(numero):
    try:
        numero = int(numero)
        numero_str = str(numero)

        if numero_str == numero_str[::-1]:
            print("El número es capicúa")
            return True
        else:
            print("El número no es capicúa")
            return False

    except ValueError:
        print("Error: debes ingresar un número válido")
        return False

def numero_perfecto(numero):
    try:
        numero = int(numero)

        if numero <= 0:
            print("El número debe ser positivo")
            return False

        suma = 0

        for i in range(1, numero):
            if numero % i == 0:
                suma += i

        if suma == numero:
            print("El número es perfecto")
            return True
        else:
            print("El número no es perfecto")
            return False

    except ValueError:
        print("Error: ingresa un número válido")
        return False