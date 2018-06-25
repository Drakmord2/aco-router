# encoding:utf-8

"""
    Otimização por colônia de formigas aplicado ao problema do caixeiro viajante
    Ant Colony Optimization for Traveling Salesman Problem
"""

import random
import math


# classe que representa uma formiga
class Formiga:
    def __init__(self, cidade):
        self.cidade = cidade
        self.solucao = []
        self.custo = None

    def obterCidade(self):
        return self.cidade

    def setCidade(self, cidade):
        self.cidade = cidade

    def obterSolucao(self):
        return self.solucao

    def setSolucao(self, solucao, custo):
        # atualiza a solução
        if not self.custo:
            self.solucao = solucao[:]
            self.custo = custo
        else:
            if custo < self.custo:
                self.solucao = solucao[:]
                self.custo = custo

    def obterCustoSolucao(self):
        return self.custo


# classe do ACO
class ACO:

    def __init__(self, grafo, num_formigas, alfa=1.0, beta=5.0,
                 iteracoes=10, evaporacao=0.5):
        self.grafo = grafo
        self.num_formigas = num_formigas
        self.alfa = alfa  # importância do feromônio
        self.beta = beta  # importância da informação heurística
        self.iteracoes = iteracoes  # quantidade de iterações
        self.evaporacao = evaporacao  # taxa de evaporação
        self.formigas = []  # lista de formigas

        lista_cidades = [cidade for cidade in range(1, self.grafo.num_vertices + 1)]
        # cria as formigas colocando cada uma em uma cidade
        for k in range(self.num_formigas):
            cidade_formiga = random.choice(lista_cidades)
            lista_cidades.remove(cidade_formiga)
            self.formigas.append(Formiga(cidade=cidade_formiga))
            if not lista_cidades:
                lista_cidades = [cidade for cidade in range(1, self.grafo.num_vertices + 1)]

        # calcula o custo guloso pra usar na inicialização do feromônio
        custo_guloso = 0.0  # custo guloso
        vertice_inicial = random.randint(1, grafo.num_vertices)  # seleciona um vértice aleatório
        vertice_corrente = vertice_inicial
        visitados = [vertice_corrente]  # lista de visitados
        while True:
            vizinhos = self.grafo.vizinhos[vertice_corrente][:]
            custos, escolhidos = [], {}
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    custo = self.grafo.obterCustoAresta(vertice_corrente, vizinho)
                    escolhidos[custo] = vizinho
                    custos.append(custo)
            if len(visitados) == self.grafo.num_vertices:
                break
            min_custo = min(custos)  # pega o menor custo da lista
            custo_guloso += min_custo  # adiciona o custo ao total
            vertice_corrente = escolhidos[min_custo]  # atualiza o vértice corrente
            visitados.append(vertice_corrente)  # marca o vértice corrente como visitado

        # adiciona o custo do último visitado ao custo_guloso
        custo_guloso += self.grafo.obterCustoAresta(visitados[-1], vertice_inicial)

        # inicializa o feromônio de todas as arestas
        for chave_aresta in self.grafo.arestas:
            feromonio = 1.0 / (self.grafo.num_vertices * custo_guloso)
            self.grafo.setFeromonioAresta(chave_aresta[0], chave_aresta[1], feromonio)

    def rodar(self):

        for it in range(self.iteracoes):

            # lista de listas com as cidades visitadas por cada formiga
            cidades_visitadas = []
            for k in range(self.num_formigas):
                # adiciona a cidade de origem de cada formiga
                cidades = [self.formigas[k].obterCidade()]
                cidades_visitadas.append(cidades)

            # para cada formiga constrói uma solução
            for k in range(self.num_formigas):
                for i in range(1, self.grafo.num_vertices):
                    # obtém todos os vizinhos que não foram visitados
                    cidades_nao_visitadas = list(
                        set(self.grafo.vizinhos[self.formigas[k].obterCidade()]) - set(cidades_visitadas[k]))

                    # somatório do conjunto de cidades não visitadas pela formiga "k"
                    # servirá para utilizar no cálculo da probabilidade
                    somatorio = 0.0
                    for cidade in cidades_nao_visitadas:
                        # calcula o feromônio
                        feromonio = self.grafo.obterFeromonioAresta(self.formigas[k].obterCidade(), cidade)
                        # obtém a distância
                        distancia = self.grafo.obterCustoAresta(self.formigas[k].obterCidade(), cidade)
                        # adiciona no somatório
                        somatorio += (math.pow(feromonio, self.alfa) * math.pow(1.0 / distancia, self.beta))

                    # probabilidades de escolher um caminho
                    probabilidades = {}

                    for cidade in cidades_nao_visitadas:
                        # calcula o feromônio
                        feromonio = self.grafo.obterFeromonioAresta(self.formigas[k].obterCidade(), cidade)
                        # obtém a distância
                        distancia = self.grafo.obterCustoAresta(self.formigas[k].obterCidade(), cidade)
                        # obtém a probabilidade
                        probabilidade = (math.pow(feromonio, self.alfa) * math.pow(1.0 / distancia, self.beta)) / (
                            somatorio if somatorio > 0 else 1)
                        # adiciona na lista de probabilidades
                        probabilidades[cidade] = probabilidade

                    # obtém a cidade escolhida
                    cidade_escolhida = max(probabilidades, key=probabilidades.get)

                    # adiciona a cidade escolhida a lista de cidades visitadas pela formiga "k"
                    cidades_visitadas[k].append(cidade_escolhida)

                # atualiza a solução encontrada pela formiga
                self.formigas[k].setSolucao(cidades_visitadas[k], self.grafo.obterCustoCaminho(cidades_visitadas[k]))

            # atualiza quantidade de feromônio
            for aresta in self.grafo.arestas:
                # somatório dos feromônios da aresta
                somatorio_feromonio = 0.0
                # para cada formiga "k"
                for k in range(self.num_formigas):
                    arestas_formiga = []
                    # gera todas as arestas percorridas da formiga "k"
                    for j in range(self.grafo.num_vertices - 1):
                        arestas_formiga.append((cidades_visitadas[k][j], cidades_visitadas[k][j + 1]))
                    # adiciona a última aresta
                    arestas_formiga.append((cidades_visitadas[k][-1], cidades_visitadas[k][0]))
                    # verifica se a aresta faz parte do caminho da formiga "k"
                    if aresta in arestas_formiga:
                        somatorio_feromonio += (1.0 / self.grafo.obterCustoCaminho(cidades_visitadas[k]))
                # calcula o novo feromônio
                novo_feromonio = (1.0 - self.evaporacao) * self.grafo.obterFeromonioAresta(aresta[0], aresta[
                    1]) + somatorio_feromonio
                # seta o novo feromônio da aresta
                self.grafo.setFeromonioAresta(aresta[0], aresta[1], novo_feromonio)

        # percorre para obter as soluções das formigas
        solucao, custo = None, None
        for k in range(self.num_formigas):
            if not solucao:
                solucao = self.formigas[k].obterSolucao()[:]
                custo = self.formigas[k].obterCustoSolucao()
            else:
                aux_custo = self.formigas[k].obterCustoSolucao()
                if aux_custo < custo:
                    solucao = self.formigas[k].obterSolucao()[:]
                    custo = aux_custo
        print('Solução final: %s | custo: %d\n' % (' -> '.join(str(i) for i in solucao), custo))
