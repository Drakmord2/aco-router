# encoding:utf-8

import googlemaps
import math
import random
from datetime import datetime

# ACO-Pants
from model.solver import Solver
from model.world import World


class AcoController:
    def __init__(self):
        pass

    def solve(self):
        nodes = [
            (0, 0, 1, 'Recife'), (1, 0, 1, 'BR-232'), (2, 0, 1, 'Caruaru'), (2, 2, 10, 'Toritama'), (4, 0, 1, 'Arcoverde'),
            (3, 0, 1, 'PE-C1'), (4, 1, 1, 'PE-A1'), (5, 2, 15, 'Salgueiro'), (5, 0, 1, 'PE-A2'), (5, -1, 15, 'Petrolandia'),
            (6, -1, 20, 'Paulo Afonso'), (6, 1, 1, 'Cabrobo'), (7, 0, 1, 'PE-CA1'), (7, 2, 1, 'PE-S1'), (8, 1, 1, 'BR-428'),
            (9, 0, 1, 'Petrolina')
        ]

        edges = [
            (0, 1), (1, 2), (2, 3), (2, 5), (3, 4), (5, 4), (4, 6), (4, 8), (6, 7), (7, 11),
            (7, 13), (8, 9), (8, 11), (9, 10), (10, 12), (12, 11), (12, 14), (13, 14), (14, 15)
        ]

        world = World(nodes, self.cost)

        ants = 20
        solver = Solver(ant_count=ants)
        solution = solver.solve(world)

        print("Nodes: ", len(nodes))
        print("Number of ants: ", ants)
        print("Shortest distance: ", solution.distance)

        print("Path: ")
        path = solution.tour
        for i in range(len(path)):
            print("\t"+str(i+1)+": ", path[i][3])

    # Fitness
    def cost(self, a, b):
        distance = math.sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))
        return distance * (1 / b[2])

    def request_api(self):
        gmaps = googlemaps.Client(key="API_KEY")

        result = gmaps.directions("Escola Politecnica de Pernambuco",
                                  "Quartel do Derby",
                                  mode="driving")

        return result
