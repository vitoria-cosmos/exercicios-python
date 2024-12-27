import random

pronomes = [['Eu'], ['Tu'], ['Ele'], ['Nós'], ['Vós'], ['Eles']]
pronomes_aleatorios = [random.sample(pronomes, k=1)]

verbos = ['aprender', 'gostar', 'conhecer']
verbos_preterito = ['aprendeu', 'gostou', 'conheceu']
verbos_futuro = ['aprendera', 'gostará', 'conhecerá']
verbos_aleatorios_presente = random.sample(verbos, k=1)
verbos_aleatorios_preterito = random.sample(verbos_preterito, k=1)
verbos_aleatorios_futuro = random.sample(verbos_futuro, k=1)
all_verbos_simples = [
    verbos_aleatorios_presente, verbos_aleatorios_preterito,
    verbos_aleatorios_futuro
]
all_verbos_simples_aleatorios = random.sample(all_verbos_simples, k=1)

verbos1 = ['aprendo', 'gosto', 'conheço']
verbos1_preterito = ['aprendi', 'gostei', 'conheci']
verbos1_futuro = ['aprenderei', 'gostarei', 'conhecerei']
verbos1_aleatorio_presente = random.sample(verbos1, k=1)
verbos1_aleatorio_preterito = random.sample(verbos1_preterito, k=1)
verbos1_aleatorio_futuro = random.sample(verbos1_futuro, k=1)
all_verbos1 = [
    verbos1_aleatorio_presente, verbos1_aleatorio_preterito,
    verbos1_aleatorio_futuro
]
all_verbos1_aleatorio = random.sample(all_verbos1, k=1)

verbos2_presente = ['aprendes', 'gostas', 'conheces']
verbos2_preterito = ['aprendeste', 'gostaste', 'conheceste']
verbos2_futuro = ['aprenderás', 'gostarás', 'conhecerás']
verbos2_aleatorio_presente = random.sample(verbos2_presente, k=1)
verbos2_aleatorio_preterito = random.sample(verbos2_preterito, k=1)
verbos2_aleatorio_futuro = random.sample(verbos2_futuro, k=1)
all_verbos2 = [
    verbos2_aleatorio_presente, verbos2_aleatorio_preterito,
    verbos2_aleatorio_futuro
]
all_verbos2_aleatorio = random.sample(all_verbos2, k=1)

verbos3_presente = ['aprende', 'gosta', 'conhece']
verbos3_preterito = ['aprendeu', 'gostou', 'conheceu']
verbos3_futuro = ['aprenderá', 'gostará', 'conhecerá']
verbos3_aleatorio = random.sample(verbos3_presente, k=1)
verbos3_aleatorio_presente = random.sample(verbos3_presente, k=1)
verbos3_aleatorio_preterito = random.sample(verbos3_preterito, k=1)
verbos3_aleatorio_futuro = random.sample(verbos3_futuro, k=1)
all_verbos3 = [
    verbos3_aleatorio_presente, verbos3_aleatorio_preterito,
    verbos3_aleatorio_futuro
]
all_verbos3_aleatorio = random.sample(all_verbos3, k=1)

verbos4_presente = ['aprendemos', 'gostamos', 'conhecemos']
verbos4_preterito = ['aprendemos', 'gostamos', 'conhecemos']
verbos4_futuro = ['aprenderemos', 'gostaremos', 'conheceremos']
verbos4_aleatorio = random.sample(verbos4_presente, k=1)
verbos4_aleatorio_presente = random.sample(verbos4_presente, k=1)
verbos4_aleatorio_preterito = random.sample(verbos4_preterito, k=1)
verbos4_aleatorio_futuro = random.sample(verbos4_futuro, k=1)
all_verbos4 = [
    verbos4_aleatorio_presente, verbos4_aleatorio_preterito,
    verbos4_aleatorio_futuro
]
all_verbos4_aleatorio = random.sample(all_verbos4, k=1)

verbos5_presente = ['aprendeis', 'gostais', 'conheceis']
verbos5_preterito = ['aprendeste', 'gostaste', 'conheceste']
verbos5_futuro = ['aprendereis', 'gostareis', 'conhecereis']
verbos5_aleatorio_presente = random.sample(verbos5_presente, k=1)
verbos5_aleatorio_preterito = random.sample(verbos5_preterito, k=1)
verbos5_aleatorio_futuro = random.sample(verbos5_futuro, k=1)
verbos5_aleatorio_presente = random.sample(verbos5_presente, k=1)
verbos5_aleatorio_preterito = random.sample(verbos5_preterito, k=1)
verbos5_aleatorio_futuro = random.sample(verbos5_futuro, k=1)
all_verbos5 = [
    verbos5_aleatorio_presente, verbos5_aleatorio_preterito,
    verbos5_aleatorio_futuro
]
all_verbos5_aleatorio = random.sample(all_verbos5, k=1)

verbos6_presente = ['aprendem', 'gostam', 'conhecem']
verbos6_preterito = ['aprendeste', 'gostaste', 'conheceste']
verbos6_futuro = ['aprenderão', 'gostarão', 'conhecerão']
verbos6_aleatorio = random.sample(verbos6_presente, k=1)
verbos6_aleatorio_preterito = random.sample(verbos6_preterito, k=1)
verbos6_aleatorio_futuro = random.sample(verbos6_futuro, k=1)
verbos6_aleatorio_presente = random.sample(verbos6_presente, k=1)
verbos6_aleatorio_preterito = random.sample(verbos6_preterito, k=1)
verbos6_aleatorio_futuro = random.sample(verbos6_futuro, k=1)
all_verbos6 = [
    verbos6_aleatorio_presente, verbos6_aleatorio_preterito,
    verbos6_aleatorio_futuro
]
all_verbos6_aleatorio = random.sample(all_verbos6, k=1)

adverbios = ['muito de', 'bastante de', 'pouco de']
adverbio_aleatorio = random.sample(adverbios, k=1)

substantivos = ['programação', 'javaScript', 'Python']
substantivo_aleatorio = random.sample(substantivos, k=1)

verbos_tempos = []

pronomes = [
    ['Eu', all_verbos1_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Tu', all_verbos2_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Ele', all_verbos3_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Nós', all_verbos4_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Vós', all_verbos5_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Eles', all_verbos6_aleatorio, adverbio_aleatorio, substantivo_aleatorio]
]

pronomes_singular = [
    ['Eu', all_verbos1_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Tu', all_verbos2_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Ele', all_verbos3_aleatorio, adverbio_aleatorio, substantivo_aleatorio]
]
pronomes_singular_aleatorio = random.sample(pronomes_singular, k=1)[0]

pronomes_plural = [
    ['Nós', all_verbos4_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Vós', all_verbos5_aleatorio, adverbio_aleatorio, substantivo_aleatorio],
    ['Eles', all_verbos6_aleatorio, adverbio_aleatorio, substantivo_aleatorio]
]
pronomes_plural_aleatorio = random.sample(pronomes_plural, k=1)[0]

pronomes_singular_plural = [
    pronomes_singular_aleatorio, pronomes_plural_aleatorio
]

frase_não_conjugada = f'{pronomes_aleatorios[0][0][0]} {all_verbos_simples_aleatorios[0][0]} {adverbio_aleatorio[0]} {substantivo_aleatorio[0]}'
print(frase_não_conjugada)

frase_aleatoria_conjugada = random.sample(pronomes, k=1)[0]
frase_completa_conjugada = f'{frase_aleatoria_conjugada[0]} {frase_aleatoria_conjugada[1][0][0]} {frase_aleatoria_conjugada[2][0]} {frase_aleatoria_conjugada[3][0]}'
print(frase_completa_conjugada)
print('*****' * 10)
opcao = int(
    input(
        'Você quer uma frase no singular ou plural? Digite 0 para singular e 1 para plural: '
    ))

print(
    f'Aqui a sua frase: {pronomes_singular_plural[opcao][0]} {pronomes_singular_plural[opcao][1][0][0]} {pronomes_singular_plural[opcao][2][0]} {pronomes_singular_plural[opcao][3][0]}'
)
