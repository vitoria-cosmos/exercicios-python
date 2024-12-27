nome = input('Digite seu nome completo: ')
cpf = input('Digite o seu CPF com o formato correto {XXX.XXX.XXX-XX}: ')
rua = input('Digite o nome da sua rua: ')
numero = int(input('Digite o número: '))
bairro = input('Digite o nome do bairro: ')
cidade = input('Digite o nome da cidade: ')
salario = float(input('Digite o valor do seu salário: '))

cpf_formatado = cpf.replace('.', '').replace('-', '')
primeiro_nome = nome.split()
print(
    f'Caro senhor(a) {primeiro_nome[0]}, de CPF {cpf_formatado} e endereço {rua}, {numero}, seu novo salário é R$ {salario*2:,.2f}'
)