
"""The Environment"""


class Environment(object):
    mygraph = {"1": set(["2", "3"]),
               "2": set(["1", "4"]),
               "3": set(["1", "4"]),
               "4": set(["2", "3"]),
               "5": set(["2", "3", "4", "5"]),
               "6": set(["1", "2", "6", "9"]),
               "7": set(["7", "5", "8"]),
               "8": set(["6", "8"]),
               "9": set(["4", "10"])
               }
    # distance (cost) is the sum of the 2 numbers
    cost = {["1", '2']: "3"}
    State = "2"
    Goal = "4"


"""Agent Behaviour"""
# Depth First Search


class Agent(Environment):
    def dfs(graph, start, goal):
        stack = [(start, [start])]
        p = []
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == goal:
                    p.append(path + [next])
                else:
                    stack.append((next, path + [next]))
        return p

# Breadth First Search
    def bfs(graph, start, goal):
        queue = [(start, [start])]
        p = []
        while queue:
            (vertex, path) = queue.pop(0)
            # poping 0 make it a queue
            for next in graph[vertex] - set(path):
                if next == goal:
                    p.append(path + [next])
                    return p
                    # first path returned by bfs is the shortest path
                    # we dont need to check the rest
                else:
                    queue.append((next, path + [next]))
        return p

    def __init__(self, Environment):
        print("DFS-Paths Available")
        print(Agent.dfs(Environment.mygraph, Environment.State, Environment.Goal))
        # returns all possible routes
        print("BFS-Shortest Path")
        print(Agent.bfs(Environment.mygraph, Environment.State, Environment.Goal))
        # returns shortest routes


"""Create the agent"""
theEnvironment = Environment()
theAgent = Agent(theEnvironment)
