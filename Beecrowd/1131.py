vitorias_time1 = 0
vitorias_time2 = 0
empates = 0
partidas = 0
while True:
    gols_time1, gols_time2 = map(int, input().split())
    if gols_time1 > gols_time2:
        vitorias_time1 += 1
    elif gols_time2 > gols_time1:
        vitorias_time2 += 1
    else:
        empates += 1
    partidas += 1
    novo_jogo = int(input("Novo grenal (1-sim 2-nao)\n"))
    if novo_jogo == 2:
        break

print(f"{partidas} grenais")
print(f"Inter:{vitorias_time1}")
print(f"Gremio:{vitorias_time2}")
print(f"Empates:{empates}")
if vitorias_time1 > vitorias_time2:
    print("Inter venceu mais")
elif vitorias_time2 > vitorias_time1:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")