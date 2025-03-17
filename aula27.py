pessoas = {
    'nome': 'Moises',
    'sobrenome': 'Drumond',
    'último_nome': 'Pereira',
}

for chave, item in pessoas.items():
    print(chave, item)
print(len(pessoas))

# pessoas.setdefault('idade', 20)
# print(pessoas['idade'])
print(pessoas.get('idade'))