import random
class Environment(object):
    def __init__(self):
        self.locationCondition = {'A' : '0', 'B' : '0'}
        self.locationCondition['A'] = random.randint(0,1)
        self.locationCondition['B'] = random.randint(0,1)

class MyAgent(Environment):
    def __init__(self, Environment):
        print(Environment.locationCondition)
        vacuumLocation = random.randint(0,1)
        if vacuumLocation == 0:
            print("Vacuum randomly placed at location A")
            if Environment.locationCondition['A'] == 1:
                print("Location A is dirty")
                Environment.locationCondition['A'] = 0
                print("Location A cleaned. Moving to B")
                if Environment.locationCondition['B'] == 1:
                    print("Location B is dirty")
                    Environment.locationCondition['B'] = 0
                    print("Location B cleaned")
            else:
                print("Location A is clean. Moving to B")
                if Environment.locationCondition['B'] == 1:
                    print("Location B is dirty")
                    Environment.locationCondition['B'] = 0
                    print("Location B cleaned")
        
        elif vacuumLocation == 1:
            print("Vacuum randomly placed at location B")
            if Environment.locationCondition['B'] == 1:
                print("Location B is dirty")
                Environment.locationCondition['B'] = 0
                print("Location B cleaned. Moving to A")
                if Environment.locationCondition['A'] == 1:
                    print("Location A is dirty")
                    Environment.locationCondition['A'] = 0
                    print("Location A cleaned")
            else:
                print("Location B is clean. Moving to A")
                if Environment.locationCondition['A'] == 1:
                    print("Location A is dirty")
                    Environment.locationCondition['A'] = 0
                    print("Location A cleaned")
        print(Environment.locationCondition)

theEnvironment = Environment()
theAgent = MyAgent(theEnvironment)



   
        
        