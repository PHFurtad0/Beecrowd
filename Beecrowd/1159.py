X = 1
while X != 0:
    X = int(input())
    if X == 0:
        break
    if X % 2 == 0:
        Par, Soma = X, X 
        for c in range(4):
            Par += 2
            Soma += Par
        print(Soma)
    else:
        Par, Soma = X + 1, X + 1
        for c in range(4):
            Par += 2
            Soma += Par
        print(Soma)
            
