def DFS(G, inicio,fim):
    visitado = set()
    pilha = [(inicio, [inicio])] 

    while (pilha):
        v, caminho = pilha.pop()

        if v == fim:

            #encontra o fluxo minimo
            flux_minimo = float('inf')
            for i in range(len(caminho)-1):
                capacidade_residual = G[caminho[i]][caminho[i+1]][1] - G[caminho[i]][caminho[i+1]][0]
                flux_minimo = min(flux_minimo, capacidade_residual)
            return True, flux_minimo, caminho

        if v not in visitado:
            visitado.add(v)

            for u in G.get(v, {}):
                capacidade_respeitada = G[v][u][0] < G[v][u][1]

                if u not in visitado and capacidade_respeitada :
                    pilha.append((u, caminho + [u]))

    return False, 0, []



def FordFulkerson(G, s, t):


    # Definindo todos os fluxo como 0
    for u in G:
        for v in G[u]:
            G[u][v][0] = 0


    while True:
        caminho_existe, fluxo_minimo, caminho = DFS(G, s, t)
        if not caminho_existe:
            break

        if caminho_existe:
            for k in range(len(caminho) - 1):
                u = caminho[k]
                v = caminho[k+1]

                G[u][v][0] += fluxo_minimo

                if v not in G:
                    G[v] = {}
                if u not in G[v]:
                    G[v][u] = [0, 0]

                G[v][u][0] -= fluxo_minimo

    fluxo_total = sum(G[s][v][0] for v in G[s])
    
    return fluxo_total

def add_aresta(G,u,v,fluxo,capacidade):
        
    # if capacidade <= 0:
    #     return
    if u not in G:
        G[u] = {}
    
    G[u][v] = [fluxo, capacidade]

    return  G


def main():

    while(True):
        temp = input()
        temp = temp.split(" ")

        nTimes = int(temp[0])
        nCorrespondente = int(temp[1])
        nJogosConcluidos = int(temp[2])

        if (nTimes == nCorrespondente == nJogosConcluidos == 0):
            break  

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
                    G[cont][3][0] -= 1
                    G[cont][2] -= 1
                cont+=1


        # print(G)
        T = {}

        fonte = 's'
        sumidouro = 't'

        # Cria grafo para analizar os fluxos
        for i in range(nTimes):
            for j in range(i + 1, nTimes):

                if i == 0 or j == 0:  # <- ignora jogos do time 0
                    continue
                jogos_restantes = G[i][3][j]
                if jogos_restantes and jogos_restantes > 0:
                    node = f"jogo_{i}_{j}"
                    T = add_aresta(T,fonte,node,0,2 * jogos_restantes)

                    T = add_aresta(T, node, f'time_{i}', 0, 2 * jogos_restantes)
                    T = add_aresta(T, node, f'time_{j}', 0, 2 * jogos_restantes)

        if T == {}:
            pontuacao_zero = G[0][0]
            maior = max(G[i][0] for i in range(nTimes))
            if maior > pontuacao_zero:
                print("N")
            else:
                print("Y")
            continue
            


        w_k = G[0][0]
        r_k = G[0][2]

        algum_zero = any(max(0, w_k + r_k - G[i][0]) == 0 for i in range(1, nTimes))
        if algum_zero:
            print("N")
            continue

        for i in range(nTimes):
            if i == 0:
                continue

            # capacidade = max(0, w_k + r_k - G[i][0])
            capacidade = max(0, w_k + r_k - G[i][0] - 1)
            T = add_aresta(T, f'time_{i}', sumidouro, 0, capacidade)
        
        
        
        fluxo_total = FordFulkerson(T,fonte,sumidouro)

        soma_jogos_restantes = sum(T[fonte][jogo][1] for jogo in T[fonte])

        if fluxo_total >= soma_jogos_restantes:
            print("Y")
        else:
            print("N")



if __name__=="__main__":
    main()