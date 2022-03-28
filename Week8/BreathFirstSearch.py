# breath first search
from inspect import stack
import queue
from sre_parse import State


class Enviroment(object):
    myGraph = {"1": set(["2", "3"]),  "2": set(["1", "4"]),
               "3": set(["1", "4"]), "4": set(["2", "3"])}
    State = "2"
    goal = "4"


class Agent(Enviroment):
    def __init__(self):
        print("BFS PATH: ")
        print(Agent.BFS(Enviroment.myGraph, Enviroment.State, Enviroment.goal))

    def BFS(myGraph, State, goal):
        # use queue
        # 1st - current state, 2nd -neighbor (current state)
        queue = [(State, [State])]
        journey = []  # record journey

        # loop to know where to go next
        while queue:
            # pick wahtever is inside the queue
            # after that pick the next position to move
            (vertex, path) = queue.pop(0)
            # -set(path) to avoid revisiting
            for next in myGraph[vertex] - set(path):
                if next == goal:
                    journey.append(path + [next])
                    return journey
                else:
                    queue.append((next, path + [next]))
        return journey
# DFS


def DFS(myGraph, State, goal):
    # use queue
    # 1st - current state, 2nd -neighbor (current state)
    stack = [(State, [State])]
    journey = []  # record journey

    # loop to know where to go next
    while stack:
        # pick wahtever is inside the queue
        # after that pick the next position to move
        (vertex, path) = queue.pop(0)
        # -set(path) to avoid revisiting
        for next in myGraph[vertex] - set(path):
            if next == goal:
                journey.append(path + [next])
                # return journey
            else:
                stack.append((next, path + [next]))
    return journey


myEvn = Enviroment()
myAgent = Agent(myEvn)
