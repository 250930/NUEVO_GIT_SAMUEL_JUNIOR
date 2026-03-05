def primos_en_rango(inicio, fin):
    if inicio > fin:
        print("El valor inicial debe ser menor o igual al valor final")
        return
    
    for numero in range(inicio, fin + 1):
        if numero < 2:
            continue
        
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        
        if es_primo:
            print(numero, end=" ")

def es_primo(numero):
    if numero < 2:
        print("No es primo")
        return
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print("No es primo")
            return
        print("Es primo")
    
    return True

def factorial(n):
    if n < 0:
        print("No existe factorial para números negativos")
        return 
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        print(resultado)
    return

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a