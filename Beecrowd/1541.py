while True:
    entrada = input().split()
    a = int(entrada[0])
    if a == 0:
        break
    b = int(entrada[1])
    c = int(entrada[2])
    area = (a * b * 100) // c
    lado = int(area ** 0.5)
    print(lado)