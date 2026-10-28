num = cont = soma = 0
num = int(input('Digite um numero [777 para parar]:'))
while num!= 777:
    soma += num
    cont += 1
    num = int(input('Digite um numero [777 para parar]:'))
print(' Você digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))
