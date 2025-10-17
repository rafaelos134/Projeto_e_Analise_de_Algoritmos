def adiciona_aresta(G,u,v,flux,limit,pontucao):
    G[u] = [v,flux,limit,pontucao]



def maxValor(G,node):
    pontos = 0

    for x in G.keys():
        for y in G[x].keys():
            if x == node:
                if G[x][y][0] != 1:
                    G[x][y][0] = 1
                    G[x][y][2] = 2
                pontos += G[x][y][2]
            if x != node:
                if y == node:
                    if G[x][y][0] != 1:
                        G[x][y][0] = 1
                        G[x][y][2] = 2
                    pontos += G[x][y][2]

    return G, pontos







temp = input()
temp = temp.split(" ")

nTimes = int(temp[0])
nCorrespondente = int(temp[1])
nJogos = int(temp[2])

G = {i:{} for i in range(nTimes)}

for i in range(nTimes):
    for j in range(nTimes):
        if (i!=j ): # ou i!=j para duas direções i < j
            G[i][j] = [0,nCorrespondente,0]


for i in range(nJogos):

    temp = input()
    temp = temp.split(" ")

    nodeU = int(temp[0])
    operador = temp[1]
    nodeV = int(temp[2])

    # flux = 0
    if (operador == "<"):
        pontuacao = 2
        flux = 1
    if (operador == "="):
        pontuacao = 1
        flux = 1

    
    # for x in G:
    #     for y in x.keys():
    #         if y == nodeU:


    #     print(x.keys())
        # if x.keys == 1:
        #     print("pa")

    # 3 < 2
    G[nodeU][nodeV][0] = flux
    G[nodeU][nodeV][2] = pontuacao
    
# print(G.keys())
# print(G[0][1])
G, pontosZero = maxValor(G,0)
print(f"pontos zero: {pontosZero}")
print(G)

for x in range(1,nTimes):
    T = G
    T, pontosAtual = maxValor(T,x)

    print(f"GRAFO MAX DE {x}: {T}")
    # print(pontosAtual)

    if pontosZero < pontosAtual:
        print("perdeu mane!")

