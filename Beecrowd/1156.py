s = 1
N = 1
D = 1
for i in range(1,19):
    N += 2
    D *= 2
    s += N/D

print(f'{s:.2f}')
    