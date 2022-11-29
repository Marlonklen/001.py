valor = []
valorimp = []
valorpar = []
while True:
    valor.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(valor):
    if v % 2 == 0:
        valorpar.append(v)
    else:
        valorimp.append(v)
print(f'Sua lista completa é {valor}')
print(f'Sua lista de pares é {valorpar}')
print(f'Sua Lista de impares é {valorimp}')
