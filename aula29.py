p1 = {
    # 'nome': 'Moises',
    'sobrenome': 'Drumond',
}

print(p1.get('nome', 'Não existe')) # define como padrão igual ao setdefault, caso não ache,
# mas só para essa função, logo, se eu der mais um print de p1['nome'] não funcionará.

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)

# método update mto importante. Retorna sempre em dict, mesmo nos casos acima de listas e tuplas
