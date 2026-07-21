from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento?'))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade <= 25:
    print('CATEGORIA: SENIOR')
else:
    print('CATEGORIA: MASTER')
