print("Será que são divisiveis?")
print('='*100)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

resultado = n1 % n2

if resultado == 0 :
    print("{} é divisivél por {}".format(n1,n2))
else:
    print("{} não é divisivél por {}".format(n1,n2))