n1 = float(input('Primeira nota?'))
n2 = float(input('Segunda nota?'))
media = (n1 + n2) / 2
if media >= 7.0:
    print(' Parábens você esta aprovado! sua media foi {:.2f}'.format(media))
elif media > 5.0 < 6.9:
    print('Você esta de recuperação sua media foi {:.2f}'.format(media))
else:
    print('você esta reprovado! sua media foi {:.2f}'.format(media))
