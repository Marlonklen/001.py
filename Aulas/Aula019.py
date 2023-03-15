pessoas = {'Nome': 'marlon', 'Idade' : 26, 'sexo' : 'M'}
pessoas['Peso'] = 71.5
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-='* 20)
for k in pessoas.keys():
    print(k)

print('-='* 20)
for k in pessoas.values():
    print(k)

print('-='* 20)
for k, v in pessoas.items():
    print(f'{k} = {v}')

