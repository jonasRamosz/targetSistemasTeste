string = input('Digite a string que desejar')
lista = []
for x in string:
    lista.append(x)
for a in range(len(lista)-1,-1,-1):
    print(lista[a], end=(', '))