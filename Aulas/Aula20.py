'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma vale A + B = {s}')


# Programa principal
soma(b=4, a=5) #Comando explicito.
soma(7, 2)'''

'''def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam}.')


contador(2, 1, 3)
contador(8, 0,)
contador(4, 6, 8, 7)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 7, 9, 5, 3]
dobra(valores)
print(valores)


