distancia = float(input('Qual é a distancia da sua viagem?'))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 180:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua viagem será de R$ {:.2f}.'.format(preço))
