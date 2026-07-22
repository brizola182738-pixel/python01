peso = float(input('Qual é o seu peso?(kg)'))
altura = float(input('Qual a sua altura?(m)'))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc <18.5:
    print('Você esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('Parabens, você esta com o PESO ideal')
elif 25 <= imc < 30:
    print(' você esta em sobrepeso')
elif 30 <= imc < 40:
    print('Você esta em OBESIDADE')
elif imc >= 40:
    print('Você esta em OBESIDADE MORBIDA! CUIDADO!')




