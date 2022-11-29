palavras = ('BOLO', 'BOLA', 'FEIJAO', 'ARROZ', 'ABOBORA', 'MACARRAO', 'DEDO', 'MORANGO',
            'MARSHIMELOW', 'GARRAFA','AMIGOS','TRATOR')
for pal in palavras:
    print(f'\nNa palavra {pal} contém as vogais', end=' ')
    for vog in pal:
        if vog.upper() in 'AEIOU':
            print(vog, end=' ')


