indivíduos = 0
soma = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    indivíduos += 1
    soma += idade
if soma == 0:
    média = 0   
else:
    média = soma/indivíduos     
print(f"{média:.2f}")    