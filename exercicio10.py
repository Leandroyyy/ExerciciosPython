print("Calculos")
print('='*100)

print('Qual operação deseja realizar?')
print("="*100)

print('1.Somar dois números')
print('2.Raiz quadrada de um número')
print('='*100)

escolha = int(input("Digite o número da sua opção: "))

if escolha == 1:
    n1 = float(input("Digite o número: "))
    n2 = float(input("Digite o número: "))
    print("a soma dos número informados é: {}".format(n1+n2))
elif escolha == 2:
    raiz = float(input("Digite o número para calcular a raiz: "))
    raizQ = raiz ** (1/2)
    print("A raíz quadrada de {} é {}".format(raiz,raizQ)) 
else: 
    print("Escolha uma opção Válida!!")

