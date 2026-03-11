#Se o usuário possue o sobrenome Silva
sobren = str(input('Qual é o seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {'SILVA' in sobren.upper()}')