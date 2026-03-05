def primos_en_rango(inicio, fin):
    if inicio > fin:
        print("El valor inicial debe ser menor o igual al valor final")
        return
    
    for numero in range(inicio, fin + 1):
        if numero < 2:
            continue