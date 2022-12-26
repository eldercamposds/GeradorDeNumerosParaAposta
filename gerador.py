from random import randint
jogos = []
jogosf = []
palpite = int(input('Quantos jogos serão gerados?'))
#for p in range(0, palpite):
   # jogos.append([0, 0, 0, 0, 0, 0])
for c in range(0, palpite):
    for l in range(0, 15):
        if l >= 0:
            num = randint(1, 25)
            if num not in jogos:
                jogos.append(num)
            else:
                while num in jogos and l < 15:
                    num = randint(1, 25)
                    if num not in jogos:
                        jogos.append(num)
                        break

    jogosf.append(jogos[:])
    jogos.clear()
print(f'Foram gerados {palpite} jogos com os seguintes numeros:\n')
for l in range(0, len(jogosf)):
    print(f'Jogo número {l+1}: {jogosf[l]} ')
