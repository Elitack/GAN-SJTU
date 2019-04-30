import random

import numpy as np
import networkx as nx
import os

class Graph():
    def __init__(self, nx_G):
        self.G = nx_G
        self.nums = self.G.shape[0]

    def node2vec_walk(self, walk_length, start_node):
        '''
        Simulate a random walk starting from start node.
        '''
        G = self.G

        walk = [start_node]

        while len(walk) < walk_length:
            cur = walk[-1]
            if G[cur].any():
                walk.append(np.random.choice(self.nums, size=1, p=G[cur]/np.sum(G[cur]))[0])
            else:
                break

        return walk

    def simulate_walks(self, num_walks, walk_length):
        '''
        Repeatedly simulate random walks from each node.
        '''
        G = self.G
        walks = []
        nodes = [i for i in range(self.nums)]
        print('Walk iteration:')
        for walk_iter in range(num_walks):
            print(str(walk_iter + 1), '/', str(num_walks))
            random.shuffle(nodes)
            for node in nodes:
                walks.append(self.node2vec_walk(walk_length=walk_length, start_node=node))

        return walks