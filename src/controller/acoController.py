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
        nodes = []
        for _ in range(40):
            x = random.uniform(-10, 10)
            y = random.uniform(-10, 10)
            nodes.append((x, y))

        world = World(nodes, self.euclidean)

        solver = Solver()
        solution = solver.solve(world)

        print("Nodes: ", len(nodes))
        print("Shortest distance: ", solution.distance)
        print("Path: ")
        path = solution.tour
        for i in range(len(path)):
            print("\t"+str(i+1)+": ", path[i])

    # Fitness
    def euclidean(self, a, b):
        return math.sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))

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
