print("Bem vindo ao Banco Bradesco")
print("="*100)

senha = (input("Digite sua senha do banco: ")).upper()

senhaVerdadeira =  'FIAP1TDS'

if senha == senhaVerdadeira:
    print("Acesso permitido")
else:
    print('Você não tem acesso ao sistema')