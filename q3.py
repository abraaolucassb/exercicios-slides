'''
Implemente um exemplo de uso de função Lambda.
'''

# A função lambda em Python é uma forma de criar funções anônimas, ou seja,
# funções que não possuem um nome associado a elas. Elas são definidas utilizando
# a palavra-chave lambda, seguida pelos parâmetros de entrada separados por vírgulas,
# seguidos por dois pontos e a expressão que será retornada pela função.

# preco = 1000


# def calcular_imposto(preco):
# return preco * 0.3


# print(calcular_imposto(preco))

# COM O LAMBDA:

# calcular_imposto2 = lambda x: x * 0.3

# print(calcular_imposto2(preco))

# A função lambda é útil em situações onde precisamos definir funções de forma rápida
# e simples, sem a necessidade de criar uma função comum usando a palavra-chave def.
# Além disso, elas podem ser usadas em conjunto com outras funções que recebem funções
# como argumentos, como as funções map, filter e reduce, por exemplo.

precos = [100, 150, 200, 250]

impostos = list(map(lambda x: x*0.3, precos))

print(impostos)

# ou seja, não preciso antes definir uma função para utilizar o lambda, eu posso usar
# diretamente
