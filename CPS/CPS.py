from ast import For
import constraint
from numpy import equal

problem = constraint.Problem()
problem.addVariable("WA", ["Red", "Green", "BLue"])
problem.addVariable("NT", ["Red", "Green", "BLue"])
problem.addVariable("SA", ["Red", "Green", "BLue"])
problem.addVariable("QL", ["Red", "Green", "BLue"])
problem.addVariable("NSW", ["Red", "Green", "BLue"])
problem.addVariable("VI", ["Red", "Green", "BLue"])
problem.addVariable("TA", ["Red", "Green", "BLue"])

def myConstraint(wa, nt, sa, ql, nsw, vi, ta):
    # content of WA is not equal the content of ta
    if (wa != ta) and (wa != sa) and (sa != nt) and (ql != sa) and (ql != nt) and (ql != nsw) and (nsw != sa) and (nsw != vi) and (vi != sa) and (vi != ta):
        return True

problem.addConstraint(myConstraint, ["WA","NT","SA", "QL", "NSW", "VI", "TA"])
solutions = problem.getSolutions
for solution in solutions:
    print(solution)