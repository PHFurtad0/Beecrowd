Num = int(input())

for i in range(Num-1,0,-1):
    Fatorial = Num * i    
    Num = Fatorial
if Num == 0 or Num == 1:
    print("1")
else:
    print(Fatorial)