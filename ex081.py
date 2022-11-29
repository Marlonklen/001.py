valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'A sua lista contem {len(valor)} valores!')
valor.sort(reverse= True)
print(f'Asua lsta em ordem decrescente é {valor}')
if 5 in valor:
        print('O numero 5 foi ditado na lista')
else:
        print('O numero 5 não se encontra na lista!')




    
