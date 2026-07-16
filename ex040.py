n1 = float(input('Primeira nota?'))
n2 = float(input('Segunda nota?'))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno será {:.1f}'.format(n1, n2, media))
if media >= 7.0 :
    print(' Parábens você esta APROVADO!')
elif media > 5.0 < 7.0:
    print('Você esta de RECUPERAÇÃO!')
elif media <5.0:
    print('você esta \033[31;40m REPROVADO\033[m!')

