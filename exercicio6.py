print("Vamos descobrir que tipo é este triângulo")
print("="*100 )

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

if (n1 + n2 > n3) and (n1 + n3 > n2) and (n2 + n3 > n1):
    if n1 == n2 and n1 == n3 and n2 == n3:
        print("Este é um triângulo equilátero, ou seja, todos os lados são iguais")
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print("Este é um triângulo escaleno, ou seja, nenhum dos lados são iguais")
    else: 
        print("Este é um triângulo isóceles, ou seja, somente dois lados são iguais")
else:
    print('Estas medidas não formam um triângulo')