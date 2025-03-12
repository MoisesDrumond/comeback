import re
import sys
# 738.998.370-10 73899837010
# cpf_enviado_usuario = '738.998.370-10'\
# .replace('.', '')\
# .replace('-', '')\
# .replace(' ', '')
entrada = input('Digite seu CPF:')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[0:9]
contador_regressivo = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += contador_regressivo * int(digito)
    contador_regressivo -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_calculo= f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_calculo:
    print(f'{cpf_gerado_calculo} é um CPF válido.')
else:
    print('CPF inválido.')
