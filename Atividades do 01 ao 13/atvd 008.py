#lendo número de 0 a 9999 e mostrar uni, dez, cen e mil
'''forma de string'''
num = int(input('Digite um númeto entre 0 a 9999: '))
n = str(num)
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')