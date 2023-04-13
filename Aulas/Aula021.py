def contador(i, f, p):
    """
    ->Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Final da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}  ', end='')
        c += p
    print('FIM')

def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: o terceiro valor
    :return:
    """
    s = a + b + c
    print(f'A soma vale {s}')


contador(2, 10, 2)
soma(a = 1, c = 2)

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 de fora vale {n1}')


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')


def somar (a = 0, b = 0, c = 0):
    s = a + b + c
    return(s)


r1 = somar(1, 7, 9)
r2 = somar(3, 8)
r3 = 8
print(f'Os rsultados foram {r1}, {r2} e {r3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print('é Par')
else:
    print('não é par.')