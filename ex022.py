nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minisculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {}'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))


