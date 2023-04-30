'''
Para que serve a palabra reservada "assert"?
'''

# O assert em Python é uma declaração que pode ser usada para verificar se
# uma determinada condição é verdadeira durante a execução de um programa.
# A declaração assert é útil para depurar o código, pois permite ao programador
# detectar erros lógicos e problemas em tempo de execução.

# basicamente o assert só funciona para desenvolvimento, não para produção
# ajuda o programa a descobrir as falhas do código

# EXEMPLO:

print('Início')

assert 1 < 2

print('Final')

# nesse exemplo verificamos se 1 é menor que dois, o código vai printar as prints
# normalmente, porém, se eu trocar os números de possição, vai dar um AssertionError
# porque 2 não é menor que 1
