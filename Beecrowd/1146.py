while True:
    qtd = int(input())
    if qtd == 0:
        break
    for i in range(1,qtd+1):
        if i == qtd:
            print(i)
            break
        if i % qtd != 0:
            print(f"{i}",end=" ")