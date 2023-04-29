'''
Reescreva o item anterior com usando for.
'''

# item anterior

# precos = [100, 150, 200, 250]

# impostos = list(map(lambda x: x*0.3, precos))

# print(impostos)

precos = [100, 150, 200, 250]
impostos = []

for preco in precos:
    impostos.append(preco * 0.3)

print(impostos)

# saída: [30.0, 45.0, 60.0, 75.0]
