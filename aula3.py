velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE= 1

velocidade_carro_passou_radar = velocidade > RADAR_1
local_carro_pega_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = local_carro_pega_radar and velocidade_carro_passou_radar

if velocidade_carro_passou_radar:
    print('Carro passou a velocidade do radar 1')

if local_carro_pega_radar:
    print('Carro passou radar 1')

if local_carro_pega_radar and velocidade_carro_passou_radar:
    print('Carro multado em radar 1')
