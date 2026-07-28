from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = (int(input('Em que ano a {}ª pessoa nasceu?'.format(c))))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas MAIORES de idade'.format(maior))
print('E tambem tivemos {} pessoas MENORES de idade'.format(menor))





