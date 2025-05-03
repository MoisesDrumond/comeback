class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Moises', 'Drumond')
p2 = Pessoa('Pedro', 'Queiroga')

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)