def adiciona_aresta(G,u,v,flux,limit,pontucao):
    G[u] = [v,flux,limit,pontucao]


inteiro = input()

inteiro = inteiro.split(" ")

nTimes = int(inteiro[0])
nCorrespondente = int(inteiro[1])
nJogos = int(inteiro[2])

G = {}


for i in range(nTimes):
    G[i] = []
    for j in range(nTimes):
        if (i != j):
            G[i].append([j,0,nCorrespondente,0])

print(G)