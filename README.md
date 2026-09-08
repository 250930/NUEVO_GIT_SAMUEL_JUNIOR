# Calculadora Matemática en Python

Este proyecto es una calculadora matemática en consola desarrollada en Python que permite ejecutar diferentes operaciones matemáticas mediante un menú interactivo. El programa fue realizado de forma colaborativa utilizando Git y GitHub.

Estructura del proyecto

calculadora-matematica/
main.py
usuario_a.py
usuario_b.py
README.md

Archivos

main.py  
Contiene el menú interactivo desde donde el usuario puede seleccionar la operación que desea ejecutar.

usuario_a.py  
Contiene las funciones desarrolladas por el usuario A:
- Serie Fibonacci
- Número Capicúa
- Número Perfecto

usuario_b.py  
Contiene las funciones desarrolladas por el usuario B:
- Primos en un rango
- Verificar si un número es primo
- Factorial
- Máximo Común Divisor (MCD)

Funciones del programa

Usuario A

Serie Fibonacci  
Genera los primeros números de la serie de Fibonacci.

Número Capicúa  
Determina si un número se lee igual de izquierda a derecha y viceversa.

Número Perfecto  
Determina si la suma de los divisores propios de un número es igual al mismo número.

Usuario B

Primos en un rango  
Muestra todos los números primos entre un valor inicial y un valor final.

Verificar si un número es primo  
Determina si un número ingresado es primo o no.

Factorial  
Calcula el factorial de un número entero positivo.

Máximo Común Divisor (MCD)  
Calcula el máximo común divisor entre dos números usando el algoritmo de Euclides.

Ejecución del programa

Para ejecutar el programa usa el siguiente comando:

python main.py

Luego selecciona la opción deseada en el menú.

Requisitos

Python 3
Terminal o consola
Git

Tecnologías utilizadas

Python  
Git  
GitHub  
Programación modular

Objetivo del proyecto

Practicar funciones en Python, aplicar programación modular y trabajar de forma colaborativa utilizando
 
USE inmobiliaria_db;

-- =====================================================
-- CONSULTA 1
-- Mostrar todos los clientes junto al total pagado
-- en el mes actual
-- =====================================================

SELECT
    c.id_cliente,
    c.nombres,
    c.apellidos,
    IFNULL(SUM(p.monto_pagado), 0) AS total_pagado_mes
FROM cliente c
LEFT JOIN contrato ct
    ON c.id_cliente = ct.id_cliente
LEFT JOIN pago p
    ON ct.id_contrato = p.id_contrato
    AND MONTH(p.fecha_pago) = MONTH(CURDATE())
    AND YEAR(p.fecha_pago) = YEAR(CURDATE())
GROUP BY
    c.id_cliente,
    c.nombres,
    c.apellidos;


-- =====================================================
-- CONSULTA 2
-- Pagos cuya fecha programada es mayor al día actual
-- y tienen estado Pendiente
-- =====================================================

SELECT
    p.id_pago,
    p.numero_recibo,
    p.monto_pagado,
    p.fecha_programada,
    ep.nombre AS estado
FROM pago p
JOIN estado_pago ep
    ON p.id_estado_pago = ep.id_estado_pago
WHERE p.fecha_programada > CURDATE()
AND ep.nombre = 'Pendiente';


-- =====================================================
-- CONSULTA 3
-- Clientes con más de 2 pagos atrasados
-- Usando subconsulta con COUNT(*)
-- =====================================================

SELECT
    c.id_cliente,
    c.nombres,
    c.apellidos
FROM cliente c
WHERE (
    SELECT COUNT(*)
    FROM contrato ct
    JOIN pago p
        ON ct.id_contrato = p.id_contrato
    JOIN estado_pago ep
        ON p.id_estado_pago = ep.id_estado_pago
    WHERE ct.id_cliente = c.id_cliente
    AND ep.nombre = 'Atrasado'
) > 2;


-- =====================================================
-- CONSULTA 4
-- Trigger actualizar_estado_pago
-- Si el pago ya venció y sigue Pendiente,
-- cambia automáticamente a Atrasado
-- =====================================================

DROP TRIGGER IF EXISTS actualizar_estado_pago;

DELIMITER $$

CREATE TRIGGER actualizar_estado_pago
BEFORE UPDATE ON pago
FOR EACH ROW
BEGIN

    IF NEW.fecha_programada < CURDATE()
       AND NEW.id_estado_pago = (
            SELECT id_estado_pago
            FROM estado_pago
            WHERE nombre = 'Pendiente'
            LIMIT 1
       )
    THEN

        SET NEW.id_estado_pago = (
            SELECT id_estado_pago
            FROM estado_pago
            WHERE nombre = 'Atrasado'
            LIMIT 1
        );

    END IF;

END$$

DELIMITER ;


-- =====================================================
-- CONSULTA 5
-- Nombre del cliente, teléfono y número total
-- de propiedades arrendadas
-- =====================================================

SELECT
    c.id_cliente,
    CONCAT(c.nombres, ' ', c.apellidos) AS nombre_cliente,
    c.telefono,
    COUNT(DISTINCT ct.id_propiedad) AS total_propiedades_arrendadas
FROM cliente c
LEFT JOIN contrato ct
    ON c.id_cliente = ct.id_cliente
GROUP BY
    c.id_cliente,
    c.nombres,
    c.apellidos,
    c.telefono;