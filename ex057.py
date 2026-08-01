sexo = str(input('Me informe o seu sexo:[M/F]')).strip().upper()[0]
while sexo not in 'M/F':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


