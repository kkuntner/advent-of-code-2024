print("Welcome to Day 223. The end is here soon! :)")

from collections import defaultdict
import numpy as np
import os
import heapq
import networkx as nx

import time


def load_input(input_file):
    graph = dict()

    with open(input_file, 'r') as f:
        # read line by line
        while line := f.readline().strip():
            nodes= line.split('-')
            if nodes[0] not in graph:
                graph[nodes[0]] = [nodes[1]]
            else:
                graph[nodes[0]].append(nodes[1])
            if nodes[1] not in graph:
                graph[nodes[1]] = [nodes[0]]
            else:
                graph[nodes[1]].append(nodes[0])

    return graph



def count_triangles(graph):
    result = 0
    for node in graph:
        for neighbor in graph[node]:
            for neighbor2 in graph[neighbor]:
                if neighbor2 in graph[node]:
                    if node.startswith('t') or neighbor.startswith('t') or neighbor2.startswith('t'):
                        print(f"triangle: {node} - {neighbor} - {neighbor2}")
                        result += 1
    return result / 6

def do1(graph):
    result = 0

    result = count_triangles(graph)

    return result


def do2(graph):
    result = ""

    #use networkx... why reinvent the wheel? :)
    g = nx.Graph()
    for node in graph:
        for neighbor in graph[node]:
            g.add_edge(node, neighbor)

    cliques = list(nx.find_cliques(g))

    party = max(cliques, key=len)
    
    party.sort()
    
    # join the party, comma separated
    result = ",".join(party)

    return result
        
# this year I won't figure out how to look for local file in VS Code :)
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\23\input.txt'   

graph = load_input(input_file)

t1 = time.time()
result = do1(graph)
print(f"Result: {result}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
result2 = do2(graph)
print(f"result: {result2}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")