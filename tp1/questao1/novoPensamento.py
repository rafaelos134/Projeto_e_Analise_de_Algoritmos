


def main():

    # while(True):


    # if (nTimes == nCorrespondente == nJogosConcluidos == 0):
    #     break


    temp = input()
    temp = temp.split(" ")

    nTimes = int(temp[0])
    nCorrespondente = int(temp[1])
    nJogosConcluidos = int(temp[2])

    v = 0 
    d = 0  
    r = nCorrespondente*(nTimes -1)
    G = []

    # Monta tabela de times e partidas
    for i in range(nTimes):
        jogos_time = []

        for j in range(nTimes):
            if i != j:
                jogos_time.append(nCorrespondente)  
            else:
                jogos_time.append(None)  

        G.append([v, d, r, jogos_time])


    for i in range(nJogosConcluidos):

        temp = input()
        temp = temp.split(" ")

        nodeU = int(temp[0])
        operador = temp[1]
        nodeV = int(temp[2])

        if (operador == "<"):

            G[nodeV][0] += 2 
            G[nodeU][1] += 1
            G[nodeU][2] -= 1
            G[nodeV][2] -= 1

            G[nodeV][3][nodeU] -= 1
            G[nodeU][3][nodeV] -= 1  

        else:
            G[nodeV][0] += 1 
            G[nodeU][0] += 1
            G[nodeU][2] -= 1
            G[nodeV][2] -= 1

            G[nodeV][3][nodeU] -= 1
            G[nodeU][3][nodeV] -= 1  

    # fazendo 0 ganhar todas
    if G[0][2] != 0:
        for i in range(G[0][2]):
            G[0][0] += 2
            G[0][2] -= 1

        cont = 0
        for i in G[0][3]:
            if i != 0 and i != None:
                G[0][3][cont] -= 1 
            cont+=1

    print(G)
    # for i in range(nTimes):
    #     for j in range(nTimes):
    #         if (i!=j ): # ou i!=j para duas direções i < j
    #             G[i] = [0,0,nCorrespondente,[]]
    #             flux = 1
    #             G[nodeV][nodeU][0] += flux
    #             G[nodeU][nodeV][0] += flux
    #             G[nodeV][nodeU][2] += pontuacao


    #         if (operador == "="):
    #             pontuacao = 1
    #             flux = 1
    #             G[nodeV][nodeU][0] += flux
    #             G[nodeU][nodeV][0] += flux
    #             G[nodeU][nodeV][2] += pontuacao
    #             G[nodeV][nodeU][2] += pontuacao

    #     flux = 0
    #     limite = nCorrespondente



    #     G, pontosZero = maxValor(G,0,flux,limite)

    # pontucao = []


    return 0

if __name__=="__main__":
    main()