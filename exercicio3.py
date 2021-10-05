print("Qual número é o maior??")
print("="*100)


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número ({}) é maior que o segundo ({})'.format(n1,n2))
else:
    print('O segundo número ({}) é maior que o primeiro ({})'.format(n2,n1))
