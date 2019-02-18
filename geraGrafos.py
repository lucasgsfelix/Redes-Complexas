import igraph
import random
import sys

def addEdges(graph, probability):

	''' Responsible for add an edge based on a given probability '''

	for i in graph.vs():
		for j in graph.vs():
			if random.uniform(0, 1) < probability:
				### in this case I add a edge
				graph.add_edge(i, j)

	return graph



if __name__ == '__main__':
	
	random.seed()
	probability, numVertex, namePlot_output = float(sys.argv[2]), int(sys.argv[1]), sys.argv[3]

	graph = igraph.Graph() ### declaring a graph
	graph.add_vertices(numVertex)
	graph = addEdges(graph, probability)
	output = igraph.plot(graph, target = namePlot_output+'.png')

