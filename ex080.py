num = []
for pos in range(0, 5):
    n = int(input('Digite um numero: '))
    if pos == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado ao final da lista!!')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Adaicionado a posição {pos} da lista!!')
                break
            pos += 1

print(num)