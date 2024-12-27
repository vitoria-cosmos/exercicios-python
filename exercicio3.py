print(10 * '')
print('Cadastro 1:')
nome1 = input("Digite seu nome completo: ")
cpf1 = input("Digite seu cpf sem formatação: ")
rua1 = input("Digite a sua rua: ")
num1 = input("Digite o número da sua casa: ")
bairro1 = input("Digite o seu bairro: ")
cidade1 = input("Digite a sua cidade: ")
salario1 = input("Digite o seu salário: ")

print(10 * '')
print('Cadastro 2:')
nome2 = input("Digite seu nome completo: ")
cpf2 = input("Digite seu cpf sem formatação: ")
rua2 = input("Digite a sua rua: ")
num2 = input("Digite o número da sua casa: ")
bairro2 = input("Digite o seu bairro: ")
cidade2 = input("Digite a sua cidade: ")
salario2 = input("Digite o seu salário: ")

print(10 * '')
print('Cadastro 3:')
nome3 = input("Digite seu nome completo: ")
cpf3 = input("Digite seu cpf sem formatação: ")
rua3 = input("Digite a sua rua: ")
num3 = input("Digite o número da sua casa: ")
bairro3 = input("Digite o seu bairro: ")
cidade3 = input("Digite a sua cidade: ")
salario3 = input("Digite o seu salário: ")

print(10 * '')
print('Cadastro 4:')
nome4 = input("Digite seu nome completo: ")
cpf4 = input("Digite seu cpf sem formatação: ")
rua4 = input("Digite a sua rua: ")
num1 = input("Digite o número da sua casa: ")
bairro4 = input("Digite o seu bairro: ")
cidade4 = input("Digite a sua cidade: ")
salario4 = input("Digite o seu salário: ")

print(10 * '')
print('Cadastro 5:')
nome5 = input("Digite seu nome completo: ")
cpf5 = input("Digite seu cpf sem formatação: ")
rua5 = input("Digite a sua rua: ")
num5 = input("Digite o número da sua casa: ")
bairro5 = input("Digite o seu bairro: ")
cidade5 = input("Digite a sua cidade: ")
salario5 = input("Digite o seu salário: ")

cpf_formatado1 = f'{cpf1[:3]}.{cpf1[3:6]}.{cpf1[6:9]}-{cpf1[9:]}'
nome_formatado1 = nome1.split()[0]

cpf_formatado2 = f'{cpf2[:3]}.{cpf2[3:6]}.{cpf2[6:9]}-{cpf2[9:]}'
nome_formatado2 = nome2.split()[0]

cpf_formatado3 = f'{cpf3[:3]}.{cpf3[3:6]}.{cpf3[6:9]}-{cpf3[9:]}'
nome_formatado3 = nome3.split()[0]

cpf_formatado4 = f'{cpf4[:3]}.{cpf4[3:6]}.{cpf4[6:9]}-{cpf4[9:]}'
nome_formatado4 = nome4.split()[0]

cpf_formatado5 = f'{cpf5[:3]}.{cpf5[3:6]}.{cpf5[6:9]}-{cpf5[9:]}'
nome_formatado5 = nome5.split()[0]

print(20 * '')
print(
    f'O 1° cliente cadastrado foi o(a) senhor(a) {nome_formatado1}, com o cpf {cpf_formatado1}, morando na rua {rua1} e com o salário de {len(salario1) * ""}.'
)

print(
    f'O 2° cliente cadastrado foi o(a) senhor(a) {nome_formatado2}, com o cpf {cpf_formatado2}, morando na rua {rua2} e com o salário de {len(salario2) * ""}.'
)

print(
    f'O 3° cliente cadastrado foi o(a) senhor(a) {nome_formatado3}, com o cpf {cpf_formatado3}, morando na rua {rua3} e com o salário de {len(salario3) * ""}.'
)

print(
    f'O 4° cliente cadastrado foi o(a) senhor(a) {nome_formatado4}, com o cpf {cpf_formatado4}, morando na rua {rua4} e com o salário de {len(salario4) * ""}.'
)

print(
    f'O 5° cliente cadastrado foi o(a) senhor(a) {nome_formatado5}, com o cpf {cpf_formatado5}, morando na rua {rua5} e com o salário de {len(salario5) * ""}.'
)