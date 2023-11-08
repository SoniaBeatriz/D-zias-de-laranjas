quantidade = int(input('quantas laranjas?\n'))
duzias = quantidade // 12
valor = (quantidade * 0.69)
#print('{}\n{}' .format(duzias, valor))
print(f'{duzias}\no preço é: {valor:.2f}')