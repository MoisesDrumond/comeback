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

porshe = Carro('Azera')
factory = Fabricante('Hyundai')
motoring = Motor('Honda')

porshe.motor = motoring
porshe.fabricante = factory

print(porshe.nome, porshe.motor.nome, porshe.fabricante.nome)