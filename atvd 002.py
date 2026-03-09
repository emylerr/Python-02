import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(co, ca)
print(f'A hipotenusa é {hip:.2f}')
