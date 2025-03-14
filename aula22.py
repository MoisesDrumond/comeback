# def multi(x,y,z):
#     sexo = x * y * z
#     return sexo
# multiplicar = multi(1, 2, 3)
# print(multiplicar)

def multiplication(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplica = multiplication(1, 2, 3, 4, 5, 6)
print(multiplica)
