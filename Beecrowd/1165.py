Testes = int(input())
for i in range(Testes):
    Num = int(input())
    Primo = 0
    for c in range(1,Num+1):
        if Num % c == 0:
            Primo += 1
    if Primo == 2:
        print(f'{Num} eh primo')
    else:
        print(f'{Num} nao eh primo')