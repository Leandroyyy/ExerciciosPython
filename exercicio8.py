print('Onde seu número esta ?')
print('=' * 100)

numero = float(input('Digite um número: '))

if numero >=0 and numero <= 30:
    print("Seu número está entre 0 e 30")
elif numero >= 40 and numero <= 79:
    print("Seu número está entre 40 e 79")
else: 
    print('O número informado está fora dos limites estabelecidos')