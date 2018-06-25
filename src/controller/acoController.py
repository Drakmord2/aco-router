# encoding:utf-8

import googlemaps
from datetime import datetime
from model.grafo import Grafo
from model.aco import ACO


class AcoController:
    def __init__(self):
        pass

    def solve(self):
        # cria um grafo passando o número de vértices
        grafo = Grafo(num_vertices=8)

        # mapeando cidades para números
        d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
        # adiciona as arestas
        grafo.adicionarAresta(d['B'], d['A'], 42)
        grafo.adicionarAresta(d['A'], d['B'], 42)
        grafo.adicionarAresta(d['C'], d['A'], 61)
        grafo.adicionarAresta(d['A'], d['C'], 61)
        grafo.adicionarAresta(d['C'], d['B'], 14)
        grafo.adicionarAresta(d['B'], d['C'], 14)
        grafo.adicionarAresta(d['D'], d['A'], 30)
        grafo.adicionarAresta(d['A'], d['D'], 30)
        grafo.adicionarAresta(d['D'], d['B'], 87)
        grafo.adicionarAresta(d['B'], d['D'], 87)
        grafo.adicionarAresta(d['D'], d['C'], 20)
        grafo.adicionarAresta(d['C'], d['D'], 20)
        grafo.adicionarAresta(d['E'], d['A'], 17)
        grafo.adicionarAresta(d['A'], d['E'], 17)
        grafo.adicionarAresta(d['E'], d['B'], 28)
        grafo.adicionarAresta(d['B'], d['E'], 28)
        grafo.adicionarAresta(d['E'], d['C'], 81)
        grafo.adicionarAresta(d['C'], d['E'], 81)
        grafo.adicionarAresta(d['E'], d['D'], 34)
        grafo.adicionarAresta(d['D'], d['E'], 34)
        grafo.adicionarAresta(d['F'], d['A'], 82)
        grafo.adicionarAresta(d['A'], d['F'], 82)
        grafo.adicionarAresta(d['F'], d['B'], 70)
        grafo.adicionarAresta(d['B'], d['F'], 70)
        grafo.adicionarAresta(d['F'], d['C'], 21)
        grafo.adicionarAresta(d['C'], d['F'], 21)
        grafo.adicionarAresta(d['F'], d['D'], 33)
        grafo.adicionarAresta(d['D'], d['F'], 33)
        grafo.adicionarAresta(d['F'], d['E'], 41)
        grafo.adicionarAresta(d['E'], d['F'], 41)
        grafo.adicionarAresta(d['G'], d['A'], 31)
        grafo.adicionarAresta(d['A'], d['G'], 31)
        grafo.adicionarAresta(d['G'], d['B'], 19)
        grafo.adicionarAresta(d['B'], d['G'], 19)
        grafo.adicionarAresta(d['G'], d['C'], 8)
        grafo.adicionarAresta(d['C'], d['G'], 8)
        grafo.adicionarAresta(d['G'], d['D'], 91)
        grafo.adicionarAresta(d['D'], d['G'], 91)
        grafo.adicionarAresta(d['G'], d['E'], 34)
        grafo.adicionarAresta(d['E'], d['G'], 34)
        grafo.adicionarAresta(d['G'], d['F'], 19)
        grafo.adicionarAresta(d['F'], d['G'], 19)
        grafo.adicionarAresta(d['H'], d['A'], 11)
        grafo.adicionarAresta(d['A'], d['H'], 11)
        grafo.adicionarAresta(d['H'], d['B'], 33)
        grafo.adicionarAresta(d['B'], d['H'], 33)
        grafo.adicionarAresta(d['H'], d['C'], 29)
        grafo.adicionarAresta(d['C'], d['H'], 29)
        grafo.adicionarAresta(d['H'], d['D'], 10)
        grafo.adicionarAresta(d['D'], d['H'], 10)
        grafo.adicionarAresta(d['H'], d['E'], 82)
        grafo.adicionarAresta(d['E'], d['H'], 82)
        grafo.adicionarAresta(d['H'], d['F'], 32)
        grafo.adicionarAresta(d['F'], d['H'], 32)
        grafo.adicionarAresta(d['H'], d['G'], 59)
        grafo.adicionarAresta(d['G'], d['H'], 59)

        # cria uma instância de ACO
        aco = ACO(grafo=grafo, num_formigas=grafo.num_vertices, alfa=1.0, beta=5.0,
                  iteracoes=1000, evaporacao=0.5)
        # roda o algoritmo
        aco.rodar()

        # teste com grafo completo
        '''
        num_vertices = 20
        print('Teste de grafo com %d vertices...\n' % num_vertices)
        grafo_completo = GrafoCompleto(num_vertices=num_vertices)
        grafo_completo.gerar()
        aco2 = ACO(grafo=grafo_completo, num_formigas=grafo_completo.num_vertices, 
                    alfa=1, beta=5, iteracoes=100, evaporacao=0.5)
        aco2.rodar()
        '''

    def request_api(self):
        gmaps = googlemaps.Client(key="AIzaSyAAI5GY1EGnoLFBZMet8M0pafaD7fNn7so")

        # Request directions via public transit
        now = datetime.now()
        directions_result = gmaps.directions("Sydney Town Hall",
                                             "Parramatta, NSW",
                                             mode="transit",
                                             departure_time=now)
        print(directions_result)

        return directions_result
