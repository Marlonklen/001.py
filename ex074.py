from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10),
           randint(1,10))
print('Os numeros sorteados são:', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO menor valor digitado é: {min(numeros)}')
print(f'O maior valor digitado é: {max(numeros)}')




