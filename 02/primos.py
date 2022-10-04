"""
un numero primo debe ser mayor 1 y que solo sea divisible por 1 y por si mismo
la funcion debe tomar un numero y debe retornar True si es primo o False en 
caso contrario.

sumar a todos los numeros primos.
"""
import math


def es_primo(num):
    # numeros menores que no son primos
    if num < 2:
        return False

    for n in range(2, math.floor(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
        return True


def suma_de_primos(nums):
    return sum([x for x in nums if es_primo(x)])
