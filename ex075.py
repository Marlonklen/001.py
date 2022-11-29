par = ()
numeros = (int(input('Digite um numero:')), int(input('Digite um numero:')), int(input('Digite um numero:')),
           int(input('Digite um numero:')))
print(f'Você digitou {numeros.count(9)} vez(es) o numero 9')
if 3 in numeros:
    print(f'O numero 3 foi digitado na {numeros.index(3)+1}ª posição')
else:
    print('não foi digitado nenhum valor 3')
print(f'Os valores pares digitados foram', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
