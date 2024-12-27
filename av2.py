resposta1 = ['acertou', 'errou']

resposta2 = ['errou', 'acertou']

resposta3 = ['acertou', 'errou']

p1 = int(input('Responda 0 para sim e 1 para não: 2 + 2 = 4? '))
print(f'Seu resltado:  {resposta1[p1]}')

p2 = int(input('Responda 0 para sim e 1 para não: 2 * 2 = 5? '))
print(f'Seu resltado: {resposta2[p2]}')

p3 = int(input('Responda 0 para sim e 1 para não: 2 / 2 = 1? '))
print(f'Seu resltado: {resposta3[p3]}')

pergunta_usuario = input('Digite sua pergunta: ')
resposta_sim = input('Digite a resposta para o sim: ')
resposta_nao = input('Digite a resposta para o não: ')

resposta4 = [resposta_sim, resposta_nao]

resposta_usuario = int(
    input(f'Responda 0 para sim e 1 para não: {pergunta_usuario} '))
print(f'Seu resultado: {resposta4[resposta_usuario]}')

print('Obrigado por participar!')