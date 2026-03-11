#lendo número de 0 a 9999 e mostrar uni, dez, cen e mil
'''forma matemática'''
num = int(input('Me informe um valor de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"""O número {num}:
Milhar: {m}
Centena: {c}
Dezena: {d}
Unidade: {u}""")