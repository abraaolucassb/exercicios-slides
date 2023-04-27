'''
1. Explique como utilizar tratamento de exceção, demonstre através
de um código onde vai quebrar intencionalmente.
'''

# TRATAMENTO DE EXCEÇÃO
# O tratamento de exceção em Python é uma técnica para lidar com erros e falhas
# que podem ocorrer durante a execução do programa. O tratamento de exceção permite que o
# programa capture e gerencie esses erros de forma adequada, sem que o
# programa pare de executar abruptamente.

# O QUE É UM EXECEÇÃO?
# Em programação, uma exceção é um evento anormal que ocorre durante a execução de
# um programa e que interrompe o fluxo normal de execução. As exceções podem ser causadas
# por erros de programação, erros de entrada/saída, falta de recursos do sistema ou outros
# tipos de problemas.

# EXEMPLOS:
# O código a seguir vai dar o alerta: No exception type(s) specified; Mas por quê?
# Resposta:
# O erro "No exception type(s) specified" ocorre quando o bloco except não especifica o tipo
# de exceção que ele deve capturar. Isso significa que ele está capturando todas as exceções
# que podem ocorrer no bloco try, o que não é uma boa prática de programação.

'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except:
    print('Infelizmente tivemos um problema =(')

print(f'O resultado é: {r}')
'''

# masssss o código tá rodando.......

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b

except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except Exception as erro:
    print(f'Infelizmente tivemos um problema: {erro.__class__}')
else:
    print(f'O resultado é: {r}')
finally:
    print('Volte sempre!')

# O except pode ser usado várias vezes para vários tipo de exceções
# except ValueError
# except TypeError
# OU apenas:
# except(ValueError, TypeError)

# o except vai especificar meu erro como por exemplo: except ValueError, ou pode ser qualquer erro
# basta apenas colocar o except. Ele vai dizer o que acontece quando aquele erro for executado.
# E no try é o conjunto de instruções que pode ocasionar uma exceção

# RESUMINDO, o except evita que apareça aquelas mensagens feias de erro na tela
# Você consegui ligar com os erros de maneira ideal
