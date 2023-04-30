'''
Explique o que é match: case, e como é usado no python 3.11
'''

# Uma declaração de correspondência (match statement) toma uma expressão e compara
# seu valor com padrõessucessivos dados em um ou mais blocos de casos (case blocks).
# Isso é superficialmente similar auma declaração switch em C, Java ou JavaScript (
# e muitas outras linguagens), mas é mais parecido com a correspondência de padrões
# (pattern matching) em linguagens como Rust ou Haskell. Apenas o primeiro padrão
# que corresponde é executado e também pode extrair componentes (elementos de sequência
# ou atributosde objeto) do valor em variáveis.

# A forma mais simples compara um valor de assunto com um ou mais literais.


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418 | 445:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# Observe o último bloco: o "nome de variável" _ atua como um curinga e nunca deixa
# e corresponder. Se nenhum caso corresponder, nenhum dos ramos é executado.

# Você pode combinar vários literais em um único padrão usando | ("ou"):

# case 401 | 403 | 404:
    # return "Not allowed"

# Padrões podem parecer com atribuições de desempacotamento e podem ser
# usados para vincular variáveis: (tuplas)
# point is an (x, y) tuple


def ponto(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")


ponto((9, 4))


dia = 1

match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')
    case _:
        print('Dia inválido')
