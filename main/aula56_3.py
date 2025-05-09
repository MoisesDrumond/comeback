class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

ferrari = Carro('spider')
v16 = Motor('ferrari motores')
mario = Fabricante('ferrari company')

ferrari.motor = v16
ferrari.fabricante = mario

print(ferrari.nome, ferrari.motor.nome, ferrari.fabricante.nome)
print(mario.nome)