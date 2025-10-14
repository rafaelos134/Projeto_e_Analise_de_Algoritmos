def adiciona_aresta(G,u,v,flux,limit,pontucao):
    G[u] = [v,flux,limit,pontucao]



def maxValor(G,nodeU,nodes):

    for x in G:
        G[nodeU][x][0] = 2 
    for arestas in nodes:
        G[n]
    





temp = input()
temp = temp.split(" ")

nTimes = int(temp[0])
nCorrespondente = int(temp[1])
nJogos = int(temp[2])

G = [{} for _ in range(nTimes)]

print(G)
for i in range(nTimes):
    for j in range(nTimes):
        if (i != j):
            G[i][j] = [0,nCorrespondente,0]


for i in range(nJogos):

    temp = input()
    temp = temp.split(" ")

    nodeU = int(temp[0])
    operador = temp[1]
    nodeV = int(temp[2])


    if (operador == "<"):
        flux = 2
    else:
        flux = 1

    G[nodeU][nodeV][0] = flux


maxValor(G)

print(G)