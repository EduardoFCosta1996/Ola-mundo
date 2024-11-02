import random

nomes = ['Eduardo', 'Amora', 'Nala']
random.shuffle(nomes)
#print(nomes)

novos_nomes = random.sample(nomes, k=2)
print(novos_nomes)