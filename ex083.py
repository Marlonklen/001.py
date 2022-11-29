exp = str(input('Digite aqui sua expressão: '))
pilha = list()
for simb in exp:
    if simb == '(':
        pilha.append('(')
    else:
        if simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é Inválida!')



