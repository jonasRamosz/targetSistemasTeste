t1 = 1
t2 = 0
t3 = 0
fibo = []

x = int(input("Digite o teto da sequencia "))

while t3 <= x:
    print(t3,end=', ')
    fibo.append(t3)

    t3 = t1 + t2
    t1 = t2
    t2 = t3

print('')

if x in fibo:
    print(f'O numero informado ({x}) esta presente da sequencia de fibonacci')

else:
    print(f'O numero informado ({x}) NÃO esta presente da sequencia de fibonacci')






