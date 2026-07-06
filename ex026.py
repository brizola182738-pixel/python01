frase = str(input('Digite um texto:')) .upper().strip()
print('A letra A aparece {} vezes no texto.'.format(frase.count('A')))
print(' A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

