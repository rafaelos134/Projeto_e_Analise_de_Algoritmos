#include <iostream>
#include <vector>

struct graph{
    int pontucao;
    int v;
    int flux;
    int limite;
};


void addAresta(std::vector <graph> G[], int u, int v,int flux, int limit, int pontuacao){
    G[u].push_back({pontuacao,v,flux,limit});
    // G[v].push_back(graph (u,flux,limit));
}




int main() {

    int nTimes;
    int nCorrespondente;
    int nJogos;

    std::cin >> nTimes;
    std::cin >> nCorrespondente;
    std::cin >> nJogos;

    std::vector<graph> G[nTimes];
    std::vector<graph> T[nTimes];


    for (int i = 0; i < nTimes; i++) {
        for (int j = i+1; j < nTimes; j++) {
            if (i != j) {
                addAresta(G, i, j, 0, nCorrespondente,0);
            }
        }
    }



    



}
