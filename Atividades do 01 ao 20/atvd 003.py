import math
ang = float(input('Digite um valor de ângulo: '))
rad = math.radians(ang)
print(f'O ângulo é de: {ang}')
print(f'O seno é de: {math.sin(rad):.2f}')
print(f'O cosseno é de: {math.cos(rad):.2f}')
print(f'A tangente é de: {math.tan(rad):.2f}')