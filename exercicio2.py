cpf = input('Digite seu cpf com o formato correto {xxx.xxx.xxx-xx}: ')

cpf_formatado = cpf.replace('.', '').replace('-', '')

dig1 = int(cpf_formatado[0]) * 10
dig2 = int(cpf_formatado[1]) * 9
dig3 = int(cpf_formatado[2]) * 8
dig4 = int(cpf_formatado[3]) * 7
dig5 = int(cpf_formatado[4]) * 6
dig6 = int(cpf_formatado[5]) * 5
dig7 = int(cpf_formatado[6]) * 4
dig8 = int(cpf_formatado[7]) * 3
dig9 = int(cpf_formatado[8]) * 2

soma = dig1 + dig2 + dig3 + dig4 + dig5 + dig6 + dig7 + dig8 + dig9
resto = soma % 11
dv1 = 11 - resto

dig1 = int(cpf_formatado[0]) * 11
dig2 = int(cpf_formatado[1]) * 10
dig3 = int(cpf_formatado[2]) * 9
dig4 = int(cpf_formatado[3]) * 8
dig5 = int(cpf_formatado[4]) * 7
dig6 = int(cpf_formatado[5]) * 6
dig7 = int(cpf_formatado[6]) * 5
dig8 = int(cpf_formatado[7]) * 4
dig9 = int(cpf_formatado[8]) * 3
dig10 = dv1 * 2

soma2 = dig1 + dig2 + dig3 + dig4 + dig5 + dig6 + dig7 + dig8 + dig9 + dig10
resto2 = soma2 % 11
dv2 = 11 - resto2
print(f'Digito verificador recebido: {cpf_formatado[9]}{cpf_formatado[10]}')
print(f'Digito verificador calculado: {dv1}{dv2}')