from collections import defaultdict
class PathFindingProgram:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def printAllPathsUtil(self, u, d, visited, path):
		visited[u]= True
		path.append(u)
		if u == d:
			print (path)
		else:
			for i in self.graph[u]:
				if visited[i]== False:
					self.printAllPathsUtil(i, d, visited, path)
					
		path.pop()
		visited[u]= False

	def printAllPaths(self, s, d):
		visited =[False]*(self.V)
		path = []
		self.printAllPathsUtil(s, d, visited, path)

# Driver program
g = PathFindingProgram(10)
g.addEdge("S", "G")
g.addEdge("S", 1)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(4, 2)
g.addEdge(2, 1)
g.addEdge(2, 1)
g.addEdge("G", 5)
g.addEdge(4, "G")
g.addEdge(1, "G")

s = 2 ; d = 3
print ("Following are all different paths from % d to % d :" %(s, d))
g.printAllPaths(s, d)
