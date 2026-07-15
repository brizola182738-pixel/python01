nome = str(input('Qual é o seu nome ?'))
if nome == 'Edimar':
    print('Que nome lindo, combina com você!')
elif nome == 'paulo' or nome == 'jose' or nome == 'bento':
    print('Seu nome é popular')
elif nome in 'oliver scheila benicio ines murilo':
    print('Você tem um belo nome')
else:
    print('Seu nome é normal!')
print('tenha um bom dia,{}!'.format(nome))
