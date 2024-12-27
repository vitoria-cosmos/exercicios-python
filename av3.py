
import random

pronomes = [['Eu'], ['Tu'], ['Ele'], ['Nós'], ['Vós'], ['Eles']]
pronomes_aleatorios = [random.sample(pronomes, k=1)]

verbos = ['aprender', 'gostar', 'conhecer']
verbos_aleatorios = random.sample(verbos, k=1)

verbos1 = ['aprendo', 'gosto', 'conheço']
verbos1_aleatorio = random.sample(verbos1, k=1)

verbos2 = ['aprendes', 'gostas', 'conheces']
verbos2_aleatorio = random.sample(verbos2, k=1)

verbos3 = ['aprende', 'gosta', 'conhece']
verbos3_aleatorio = random.sample(verbos3, k=1)

verbos4 = ['aprendemos', 'gostamos', 'conhecemos']
verbos4_aleatorio = random.sample(verbos4, k=1)

verbos5 = ['aprendeis', 'gostais', 'conheceis']
verbos5_aleatorio = random.sample(verbos5, k=1)

verbos6 = ['aprendem', 'gostam', 'conhecem']
verbos6_aleatorio = random.sample(verbos6, k=1)

adverbios = ['muito de', 'bastante de', 'pouco de']
adverbio_aleatorio = random.sample(adverbios, k=1)

substantivos = ['programação', 'javaScript', 'Python']
substantivo_aleatorio = random.sample(substantivos, k=1)

pronomes = [
    ['Eu', verbos1_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Tu', verbos2_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Ele', verbos3_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Nós', verbos4_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Vós', verbos5_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Eles', verbos6_aleatorio, adverbio_aleatorio, substantivo_aleatorio]
]

frase_não_conjugada = f'{pronomes_aleatorios[0][0][0]} {verbos_aleatorios[0]} {adverbio_aleatorio[0]} {substantivo_aleatorio[0]}'
print(frase_não_conjugada)

frase_aleatoria_conjugada = random.sample(pronomes, k=1)[0]
frase_completa_conjugada = f'{frase_aleatoria_conjugada[0]} {frase_aleatoria_conjugada[1][0]} {frase_aleatoria_conjugada[2][0]} {frase_aleatoria_conjugada[3][0]}'
print(frase_completa_conjugada)
