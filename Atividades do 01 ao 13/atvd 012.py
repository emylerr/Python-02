#Quantas vezes as letras aparecem e posições
nome = str(input('Digite alguma frase: ')).upper().strip()
print(f'A letra A aparece {nome.count('A')} na frase.')
print(f'A primeira letra A apareceu na posição {nome.find('A')+1}')
print(f'A última letra A apareceu na posição {nome.rfind('A')+1}')