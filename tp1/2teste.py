import copy


# Erro tem haver com o flux max
def maxValor(G,node,flux,limite):
    pontos = 0


    #melhorar essa verificao pois o flux max pode ser de 0 a 4
    for adversario in G[node].keys():    
        if G[node][adversario][0] == 0:
            G[node][adversario][0] = 2 # fluxo
            G[node][adversario][2] = 4 # pontucao 4
            G[adversario][node][0] = 2 # fluxo inv

        elif G[node][adversario][0] == 1:
            G[node][adversario][0] += 1 # fluxo
            G[adversario][node][0] += 1 # fluxo inv
            G[node][adversario][2] += 2 # pontucao
        pontos += G[node][adversario][2]

    return G, pontos


def minValor(G,node):
    pontos = 0
    pontosInv = 0

    for adversario in G[node].keys():    
        if G[node][adversario][0] == 0:
            G[node][adversario][0] = 2 # fluxo
            G[adversario][node][0] = 2 #fluxo inverso
            G[node][adversario][2] = 0 # pontucao
            G[adversario][node][2] = 4 # pontucao inversa

        elif G[node][adversario][0] == 1:
            G[node][adversario][0] += 1 # fluxo
            G[adversario][node][0] += 1 # fluxo inverso
            G[node][adversario][2] += 0 # pontucao
            G[adversario][node][2] += 2 # pontucao inversa
        

        pontos += G[node][adversario][2]
        pontosInv += G[adversario][node][2]

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
        nJogosConcluidos = int(temp[2])



        if (nTimes == nCorrespondente == nJogosConcluidos == 0):
            break

        G = {i:{} for i in range(nTimes)}

        for i in range(nTimes):
            for j in range(nTimes):
                if (i!=j ): # ou i!=j para duas direções i < j
                    G[i][j] = [0,nCorrespondente,0]


        for i in range(nJogosConcluidos):

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

        flux = 0
        limite = nCorrespondente



        G, pontosZero = maxValor(G,0,flux,limite)

        

        if cont == 3:
            print(G)
            print(pontosZero)


        for x in range(1,nTimes):
            T = copy.deepcopy(G)
            T, pontosAtual = maxValor(T,x,flux,limite)

            if cont == 3:
                print(f"print do no {x}: {T}")
                print(pontosAtual)

            if pontosZero < pontosAtual:
                prov = "N"
                break
            else:
                prov = "Y"

            


        cont+=1
        print(prov)

main()