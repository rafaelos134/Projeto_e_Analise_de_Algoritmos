import copy


# DA PARA MELHORAR REMOVENDO PERCORRER TODO O GRAFO
def maxValor(G,node):
    pontos = 0

    for x in G.keys():
        for y in G[x].keys():
            if x == node:
                if G[x][y][0] == 0:
                    G[x][y][0] = 2 # fluxo
                    G[x][y][2] = 4 # pontucao
                    G[y][x][0] = 2 

                elif G[x][y][0] == 1:
                    G[x][y][0] += 1 # fluxo
                    G[y][x][0] += 1 # fluxo
                    G[x][y][2] += 2 # pontucao
                pontos += G[x][y][2]

    return G, pontos


def minValor(G,node):
    pontos = 0
    pontosInv = 0

    for x in G.keys():
        for y in G[x].keys():
            if x == node:
                if G[x][y][0] == 0:
                    G[x][y][0] = 2 # fluxo
                    G[y][x][0] = 2 #fluxo inverso
                    G[x][y][2] = 0 # pontucao
                    G[y][x][2] = 4 # pontucao inversa
                     

                elif G[x][y][0] == 1:
                    G[x][y][0] += 1 # fluxo
                    G[y][x][0] += 1 # fluxo inverso
                    G[x][y][2] += 0 # pontucao
                    G[y][x][2] += 2 # pontucao inversa
                
                pontos += G[x][y][2]
                pontosInv += G[y][x][2]

    if pontos < pontosInv:
        pontos = pontosInv
                
    return G, pontos

def main():

    cont = 1

    while(True):

        temp = input()
        temp = temp.split(" ")



        nTimes = int(temp[0])
        nCorrespondente = int(temp[1])
        nJogos = int(temp[2])



        if (nTimes == nCorrespondente == nJogos == 0):
            break

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
                G[nodeV][nodeU][0] += flux
                G[nodeU][nodeV][0] += flux
                G[nodeV][nodeU][2] += pontuacao


            if (operador == "="):
                pontuacao = 1
                flux = 1
                G[nodeV][nodeU][0] += flux
                G[nodeU][nodeV][0] += flux
                G[nodeU][nodeV][2] += pontuacao
                G[nodeV][nodeU][2] += pontuacao

        G, pontosZero = maxValor(G,0)

        

        # if cont == 9:
        #     print(G)
        #     print(pontosZero)


        for x in range(1,nTimes):
            T = copy.deepcopy(G)
            T, pontosAtual = maxValor(T,x)

            # if cont == 9:
            #     print(f"print do no {x}: {T}")
            #     print(pontosAtual)

            if pontosZero < pontosAtual:
                prov = "N"
                break
            else:
                prov = "Y"

            


        cont+=1
        print(prov)

main()