from random import randint
from time import sleep
computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens! você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no numero {}'.format(computador, jogador))
