class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def StartDestination(self, dist):
		print("Vertex \t Distance from Source")
		for node in range(self.V):
			print(node, "\t\t", dist[node])

	def minDistance(self, dist, sptSet):

		min = 1e7

		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	def cheapestRoute(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			u = self.minDistance(dist, sptSet)

			sptSet[u] = True

			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)

# Driver program
g = Graph(13)
g.graph = [
    [5, 2, 5, 6, 1, 4, 6, 4, 3, 3, 7, 2, 6],
    [6, 2, 7, 3, 3, 4, 6, 4, 1, 6, 5, 2, 5],
    [5, 1, 4, 5, 6, 1, 2, 7, 3, 3, 4, 6, 2],
    [5, 1, 4, 5, 7, 3, 2, 4, 1, 2, 7, 6, 3],
    [6, 2, 5, 6, 2, 3, 6, 4, 3, 4, 7, 1, 5],
    [5, 2, 5, 6, 1, 4, 6, 4, 3, 3, 7, 2, 6],
    [5, 2, 5, 6, 1, 4, 6, 4, 3, 3, 7, 2, 6],
    [5, 2, 5, 6, 1, 4, 6, 4, 3, 3, 7, 2, 6],
    [5, 2, 5, 6, 1, 4, 6, 4, 3, 3, 7, 2, 6],
    [5, 2, 5, 6, 1, 4, 6, 4, 3, 3, 7, 2, 6],
    [5, 2, 5, 6, 1, 4, 6, 4, 3, 3, 7, 2, 6],
    [5, 2, 5, 6, 1, 4, 6, 4, 3, 3, 7, 2, 6],
    [5, 2, 5, 6, 1, 4, 6, 4, 3, 3, 7, 2, 6]
		]

g.cheapestRoute(0)
 
