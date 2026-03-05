# main.py

from usuario_a import fibonacci, capicua, numero_perfecto
from usuario_b import primos_en_rango, es_primo, factorial, mcd


def menu():

    while True:

        print("\n=== CALCULADORA MATEMÁTICA ===")
        print("1. Serie Fibonacci")
        print("2. Número capicúa")
        print("3. Número perfecto")
        print("4. Números primos en un rango")
        print("5. Verificar si un número es primo")
        print("6. Factorial")
        print("7. Máximo Común Divisor (MCD)")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = int(input("Ingrese n: "))
            fibonacci(n)

        elif opcion == "2":
            numero = int(input("Ingrese un número: "))
            capicua(numero)

        elif opcion == "3":
            numero = int(input("Ingrese un número: "))
            numero_perfecto(numero)

        elif opcion == "4":
            inicio = int(input("Inicio del rango: "))
            fin = int(input("Fin del rango: "))
            primos_en_rango(inicio, fin)

        elif opcion == "5":
            numero = int(input("Ingrese un número: "))
            es_primo(numero)

        elif opcion == "6":
            n = int(input("Ingrese n: "))
            factorial(n)

        elif opcion == "7":
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            mcd(a, b)

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida")


menu()