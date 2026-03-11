#cadeia de textos / strings
'''lendo nome, letra maiúscula, minúscula, quantas letras e quantidade de letras sem espaços'''
nome = str(input('Me informe seu nome completo: ')).strip()
print(f'Seu nome com letras maiúsculas é: {nome.upper()}')
print(f'Seu nome com letras minúsculas é: {nome.lower()}')
print(f'Seu nome tem ao todo: {len(nome) - nome.count(' ')} letras')
#print(f'Seu primeiro nome tem: {nome.find(' ')} letras!')
sep = nome.split()
print(f'Seu primeiro nome é {nome} e ele tem: {len(sep[0])} letras')