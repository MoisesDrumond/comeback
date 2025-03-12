lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))

print(lista_enumerada)

# for item in enumerate(lista):
    # print(item) se voce fizer um for com lista enumerada direto apenas um for vai esgotar o iterador

# for item in lista_enumerada:
    # print(item) no caso de cima vc pode criar varios for, nesse aqui, voce nao pode
