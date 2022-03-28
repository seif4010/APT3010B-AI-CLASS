from constraint import *

problem = Problem()
problem.addVariable("AI", [2, 1, 3])
problem.addVariable("Physics", [5, 4, 6])
problem.addVariable("Maths", [6, 3, 2])
problem.addVariable("DB", [4, 1, 2])

def myConstraint(ai, ph, maths, db):
    if (ai != ph) and (ph != maths) and (maths != ai) and (ph != db) and (db != maths) and (db != ai) and (db != ph) and (ph != db) and (ai != maths) and (ai != db):
        return True

problem.addConstraint(myConstraint, ["AI","Physics","Maths", "DB"])
solutions = problem.getSolutions
for solution in solutions:
    print(solution)