#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <tuple>


void addAresta(std::vector <std::tuple<int,int,int>> G[], int u, int v,int flux, int limit){
    G[u].push_back(std::tuple<int, int, int>(v,flux,limit));
    G[v].push_back(std::tuple<int, int, int>(u,flux,limit));
}


//https://www.geeksforgeeks.org/competitive-programming/graph-implementation-using-stl-for-competitive-programming-set-2-weighted-graph/
void printGraph(std::vector <std::tuple<int,int,int>>  G[],int V){

    for (int u = 0; u < V; u++){
        std::cout << "Node " << u << " tem aresta com \n";

        for (auto it = G[u].begin(); it != G[u].end(); it++){
            int v;
            int flux;
            int limit;

            std::tie(v, flux, limit) = *it;
            std::cout << "\tNode " << v << " com fluxo "  << flux << " e limite "<< limit << "\n";
        }

        std::cout << "\n";
    }
}



void maxValor(std::vector <std::tuple<int,int,int>>  G[],int V,int node){

    for (int u = 0; u < V; u++){

        if (u == node){

            for (auto it = G[u].begin(); it != G[u].end(); it++){
                int v;
                int flux;
                int limit;

                std::tie(v, flux, limit) = *it;
                
                // tem q usar par e impa
                if (limit != flux){
                    std::get<1>(*it) = 4;
                }
            }
        }else{
            continue;

            // for (auto it = G[u].begin(); it != G[u].end(); it++){
                
            //     int v;
            //     int flux;
            //     int limit;

            //     std::tie(v, flux, limit) = *it;

            //     if (node == v){
            //         if (flux == 0){
            //             std::get<1>(*it) = 2;
            //         }
            //     }

            // }
        }
      
    }

}


//erro no calculo
int calculaPontos(std::vector <std::tuple<int,int,int>>  G[],int V,int node){

    int total = 0;

    for (int u = 0; u < V; u++){

        if (u == node){

            for (auto it = G[u].begin(); it != G[u].end(); it++){
                int v;
                int flux;
                int limit;

                // std::cout << v;
                
                std::tie(v, flux, limit) = *it;

                total+=flux;
            }
        }else{

            for (auto it = G[u].begin(); it != G[u].end(); it++){
                
                int v;
                int flux;
                int limit;

                std::tie(v, flux, limit) = *it;

                if (node == v){
                    total-=flux;

                }

            }
        }
    }
    
    
    return total;

}






int main() {

    int nTimes;
    int nCorrespondente;
    int nJogos;

    std::cin >> nTimes;
    std::cin >> nCorrespondente;
    std::cin >> nJogos;

    std::vector<std::tuple<int,int,int>> G[nTimes];
    std::vector<std::tuple<int,int,int>> T[nTimes];



    for (int i = 0; i < nTimes; i++) {
        for (int j = i+1; j < nTimes; j++) {
            if (i != j) {
                addAresta(G, i, j, 0, nCorrespondente*2);
            }
        }
    }



    // Define os valores dos fluxos 
    for (int i = 0; i < nJogos; i++){
        int flux;
        int nodeU;
        std::string operador;
        int nodeV;

        std::cin >> nodeU;
        std::cin >> operador;
        std::cin >> nodeV;
    
        if (operador == "<"){
            // Caso ganhe o fluxo e definido para 2
            flux = 2;
        }else{
            // Caso empate o fluxo e definido para 1
            flux = 1;
        }


        for (auto &aresta : G[nodeU]) {
            if (std::get<0>(aresta) == nodeV) {
                std::get<1>(aresta) += flux;     
                break;
            }
    }

    }



    
    printGraph(G, nTimes);

    maxValor(G,nTimes,0);

    

    int pontZero = calculaPontos(G,nTimes,0);

    std::cout <<"Pontuacao de 0 : " <<  pontZero <<std::endl;


    for (int i = 0; i < nTimes; ++i) {
        T[i] = G[i];
    }

    int pontoTime = 0;
    
    for(int i =1; i < nTimes; i++){
        
        maxValor(T,nTimes,i);

        pontoTime = calculaPontos(G,nTimes,i);

        if (pontoTime > pontZero){
            std::cout << "perdeu";
            break;}

        for (int i = 0; i < nTimes; ++i) {
            T[i] = G[i];
        }

        std::cout <<"Pontuacao de "<< i << " : " << pontoTime << std::endl;

    }

    printGraph(G, nTimes);


    if (pontoTime > pontZero){
        std::cout << "perdeu";
    }else{
        std::cout << "ganha";}


    return 0;
}

// 4 2 6
// out
// Y
// N
// Y
// Y
// Y
// N