print("Calculando o lucro")
print("="*100)

produto = float(input("Digite o valor do seu produto: "))

menorVinte = produto * 0.45
maiorVinte = produto * 0.3

if produto < 20:
    print('Você deve vender o seu produto a {}'.format(produto+menorVinte))
else:
    print("Você deve vender o seu produto a {}".format(produto+maiorVinte))
