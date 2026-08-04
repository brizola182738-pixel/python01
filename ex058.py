from operator import truediv
from random import randint
computador = randint(0, 15)
print('Acabei de pensar em um numero entre 0 e 15')
print('Séra que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador =int(input('Qual o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente outra vez!')
        elif jogador > computador:
            print('Menos... tente outra vez!')
print(' Acertou com {} tentativas'.format(palpites))
