from collections import deque

def DFS(G, inicio):
    visitado = set()
    pilha = [inicio] 

    while (pilha):
        v = pilha.pop()

        if v not in visitado:
            visitado.add(v)

            for u in G.get(v, {}):
                if u in pilha:
                    print("helo")
                    return True

                if u not in visitado:
                    pilha.append(u)

    return False









def BFS(G):
    cor = {u: "white" for u in G}
    dist = {u: float("inf") for u in G}
    pai = {u: None for u in G}

    
    for inicio in G:
        if cor[inicio] == "white":
            cor[inicio] = "gray"
            dist[inicio] = 0
            fila = deque([inicio])


            while fila:
                u =  fila.popleft()
                for v in G[u]:

                    if cor[v] == "white":
                        cor[v] = "gray"
                        dist[v] = dist[u]+1
                        pai[v] = u

                        fila.append(v)
                cor[u] = "black"
        
    return cor, dist, pai
    
def inverte_grafo(G):
    G_inv = {u: [] for u in G}
    for u in G:
        for v in G[u]:
            if v not in G_inv:
                G_inv[v] = []
            G_inv[v].append(u)
    return G_inv



# def scc(G):

#     inicio = next(iter(G))
#     print(inicio)
#     ss = DFS(G,inicio)

    # G_inv = inverte_grafo(G)

    # cor_inv, dist_inv, pai_inv = BFS(G_inv)

    # print(pai)
    # print(cor)
    # print(dist)
    # print("inv")
    # print(pai_inv)
    # print(cor_inv)
    # print(dist_inv)

    return




def add_aresta(G, u, v):
    if u not in G:  G[u] = []
    if v not in G: G[v] = []
    G[u].append(v)







def main():

    casos = int(input())

    for _ in range(casos):

        temp = input().split(" ")

        nDocumentos = int(temp[0])
        mDependencias = int(temp[1])

        G = {}

        # print(f"sao {nDocumentos} documentos e {mDependencias} dependencias")
        for i in range(mDependencias):

            temp = input().split(" ")
            
            depende = int(temp[0])
            documento = int(temp[1])
            print(f"o doc {depende} depende do documento {documento}")

            add_aresta(G, depende, documento)

        ss = DFS(G,inicio)
        print(G)


        print("-------------------")






    return 0


if __name__ == "__main__":
    main()