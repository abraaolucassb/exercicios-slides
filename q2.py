'''
Explique a função map()
'''


# map(function, iterable, *iterables)

'''
    Retorna um iterador que aplica a função a cada item iterável, gerando os resultados.
    Se argumentos adicionais de iteráveis forem passados, a função deve receber a mesma quantidade 
    de argumentos e será aplicada aos itens de todos os iteráveis em paralelo. Com múltiplos iteráveis, 
    o iterador para quando o iterável mais curto é esgotado.

    Em outras palavras, map() executa uma operação em cada item de um iterável e retorna um novo 
    iterável com os resultados dessa operação.
'''

# temos aqui um exemplo de uma função para adicionar um imposto sobre um preço de uma lista

precos = [1000, 1500, 1250, 2500]


def adicionar_imposto(preco):
    return preco * 1.1

# mas e se eu quiser adicionar o imposto para todos os itens de uma lista ao mesmo tempo?
# EXEMPLO FOR:


# precos_com_imposto = []

# for preco in precos:
    # precos_com_imposto.append(adicionar_imposto(preco))

# print(precos_com_imposto)

# # EXEMPLO COM MAP:

precos_com_imposto2 = list(map(adicionar_imposto, precos))

print(precos_com_imposto2)

# esse código vai retornar isso: <map object at 0x7fefa62ff640>
# para fazer o map retornar em formato de lista basta colocar list(map(...))
# após isso vou ter como retorno: [1100.0, 1650.0000000000002, 1375.0, 2750.0]
# basicamente o map() tá pegando um item da lista preços e passando como parâmetro para a...
# ...função adicionar_imposto
