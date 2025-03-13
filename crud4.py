import os
import sys

lista = []
while True:
    pergunta = input('[i]nserir [l]istar [a]pagar [s]air: ')
    
    if pergunta.lower() == 'i':
        nome = input('Digite seu nome: ')
        idade = input('Digite sua idade: ')
        sobre = input('Digite sua descrição: ')
        lista.append([nome, idade, sobre])

    if pergunta != 'i' or 'l' or 'a' or 's':
        print('Digite a função correta.')
        
