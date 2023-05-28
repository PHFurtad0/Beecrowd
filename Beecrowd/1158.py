Testes = int(input())
for i in range(Testes):
    Num = input() .split()
    X = int(Num[0])
    Y = int(Num[1])
    if X % 2 == 0:
        Impar, Soma = X + 1, X + 1
        for c in range(Y-1):
            Impar += 2
            Soma += Impar
        print(Soma)
    else:
        Impar, Soma = X, X
        for c in range(Y-1):
            Impar += 2
            Soma += Impar
        print(Soma)