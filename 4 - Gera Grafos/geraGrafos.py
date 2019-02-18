import igraph
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import math

def addEdges(graph, probability):

	''' Responsible for add an edge based on a given probability '''

	for i in graph.vs():
		for j in graph.vs():
			if random.uniform(0, 1) < probability:
				### in this case I add a edge
				graph.add_edge(i, j)

	return graph

def calcDistribution(graph):

	''' Responsibl for calculating the distribution of the vertex '''

	degreeValues = np.zeros(graph.vcount()) ### calculate the degree value for each node
	for index, i in enumerate(graph.vs()):
		degreeValues[index]=i.degree(mode = 'ALL')

	degreeValues = np.sort(degreeValues) ## sorting theses values
	numberOfNodes = np.zeros(np.unique(degreeValues).size) ### responsible to calculate the number of nodes
	cont,i = 0,1
	while(i<numberOfNodes.size): ### calculate the number of nodes of each degree
		if cont == 0 and i == 1 and degreeValues[i] != degreeValues[i-1]:
			numberOfNodes[i-1] = list(degreeValues).count(degreeValues[i-1])
			i=i-1
			cont = 1
		elif degreeValues[i] != degreeValues[i-1]:
			numberOfNodes[i] = list(degreeValues).count(degreeValues[i])
		i=i+1

	degreeValues = np.unique(degreeValues) ### removing repeated values

	return degreeValues, numberOfNodes


def poissonDistribution():
	''' Calculates the poisson distribution giver a number of samples '''

	t = np.arange(0, 20, 0.1)
	d = np.exp(-5)*np.power(5, t)/math.factorial(t)
	plt.plot(t, d, 'bs')
	plt.show()


	return d

def binomialDistribution():
	pass

def graphPlot(graph):

	''' Responsible for plotting the degree distribuition of the graph '''

	degreeValues, numberOfNodes = calcDistribution(graph)
	plt.plot(degreeValues, numberOfNodes, '--', color='blue')  
	plt.title("Degree Distribuition")
	plt.grid(True) 
	plt.xlabel("Degree Value")
	plt.ylabel("Number Of Nodes")
	plt.show()


if __name__ == '__main__':



	random.seed()
	probability, numVertex, namePlot_output = float(sys.argv[2]), int(sys.argv[1]), sys.argv[3]

	graph = igraph.Graph() ### declaring a graph
	graph.add_vertices(numVertex)
	graph = addEdges(graph, probability)
	output = igraph.plot(graph, target = namePlot_output+'.png')
	graphPlot(graph)



