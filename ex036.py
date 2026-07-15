casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o salario do comprador: R$'))
anos = int(input('Quantos anos o financiamento?'))
prestação = casa / ( anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')



