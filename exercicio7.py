print('Boletim escolar')
print('='*100)

nome = input("Digite o nome do aluno: ")
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
faltas = int(input("Digite a quantidade de faltas: "))


if faltas <= 20:
    media = (n1 + n2 + n3) / 3 
    if media >= 7:
        print("Parabéns você foi aprovado!!!")
    else:
        print("Infelizmente você foi reprovado por tirar notas abaixo da média")
else:
    print("infelizmente você foi reprovado por faltas")