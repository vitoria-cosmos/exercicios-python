import random

nome = input('Qual o seu nome? ')
pergunta1 = f'Responda 0 para sim e 1 para não, {nome}: 2 + 2 = 4? '
pergunta2 = f'Responda 0 para sim e 1 para não, {nome}: 2 * 2 = 5? '
pergunta3 = f'Responda 0 para sim e 1 para não, {nome}: 2 / 2 = 1? '

gabarito = [['acertou, ganhou 1 ponto', 'errou, ganhou 0 pontos', pergunta1],
            ['errou, ganhou 0 pontos', 'acertou, ganhou 1 ponto', pergunta2],
            ['acertou, ganhou 1 ponto', 'errou, ganhou 0 pontos ', pergunta3]]

perguntas_sorteadas = random.sample(gabarito, k=3)

p1 = int(input(perguntas_sorteadas[0][2]))
print(perguntas_sorteadas[0][p1])

p2 = int(input(perguntas_sorteadas[1][2]))
print(perguntas_sorteadas[1][p2])

p3 = int(input(perguntas_sorteadas[2][2]))
print(perguntas_sorteadas[2][p3])

pergunta_usuario = input('Digite sua pergunta: ')
resposta_sim = input('Digite a resposta para o sim: ')
resposta_nao = input('Digite a resposta para o não: ')

gabarito_usuario = [
    f'{resposta_sim}, ganhou 1 ponto', f'{resposta_nao}, ganhou 0 pontos',
    pergunta_usuario
]

resposta_usuario = int(
    input(f'Responda 0 para sim e 1 para não, {nome}: {pergunta_usuario} '))
print(f'Seu resultado: {gabarito_usuario[resposta_usuario]}')

texto1 = perguntas_sorteadas[0][p1]
ponto1 = texto1.split()[2]
ponto1_num = int(ponto1)

texto2 = perguntas_sorteadas[1][p2]
ponto2 = texto2.split()[2]
ponto2_num = int(ponto2)

texto3 = perguntas_sorteadas[2][p3]
ponto3 = texto3.split()[2]
ponto3_num = int(ponto3)

texto4 = gabarito_usuario[resposta_usuario]
ponto4 = texto4.split()[-2]
ponto4_num = int(ponto4)

pontuacao_total = ponto1_num + ponto2_num + ponto3_num + ponto4_num

print(f'Obrigada por participar!  Sua pontuação é: {pontuacao_total}')
