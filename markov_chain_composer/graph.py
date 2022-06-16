# The Markov Chain representation
import random

# Define the graph in terms of vertices

class Vertex:
    def __init__(self, value): # value will be the word
        self.value = value
        self.adjacent = {} # contain vertex as key, weight as value
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self, vertex, weight=0):
        # adding edge to vertex with input weight
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        # incrementing the weight of edge given
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items(): # items() allow to loop through key:value of a dict
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        # randomly select next word ***Based on weights
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]


class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        # what are the value of all the vertices?
        # return all possible words
        return set(self.vertices.key())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        # if the value isn't in the graph
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value] # get the Vertex object

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
