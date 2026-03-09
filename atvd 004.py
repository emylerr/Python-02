import random
nomes = ['Nathan', 'Gabriel', 'Rafael', 'Ismael']
print(*nomes, sep=', ')
sort = random.choice(nomes)
print(f'O nome sorteado foi: {sort}!')