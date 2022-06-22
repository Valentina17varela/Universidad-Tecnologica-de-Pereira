import random
import sys

class CSP():
    def __init__(self, variables, domains, neighbors, constraints):

        variables = variables or list(domains.keys())

        self.variables = variables

        self.domains = domains

        self.neighbors = neighbors

        self.constraints = constraints

        self.initial = ()

        self.curr_domains = None

        self.nassigns = 0

        self.numassigns = 0

    def assign(self, var, val, assignment):

        assignment[var] = val

        self.nassigns += 1
        self.numassigns = len(assignment)


    def undoassign(self, var, assignment):

        for l in range(self.nassigns + 2):
            print(" ", end="")

        self.nassigns -= 1

        if var in assignment:


            del assignment[var]

            self.numassigns = len(assignment)

    def num_conflicts(self, var, val, assignment):


        def conflict(var2):
            return (var2 in assignment and

                    not self.constraints(var, val, var2, assignment[var2]))

        return sum(conflict(v) for v in self.neighbors[var])

    def display(self, own="", assignment={}):

        print('CSP:', self, 'assignment:', assignment)

    def init_curr_domains(self):

        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def change_curr_domains(self, var, value):

        self.init_curr_domains()

        removals = [(var, a) for a in self.curr_domains[var] if a != value]

        self.curr_domains[var] = [value]

        return removals

    def prune(self, var, value, removals):

        self.curr_domains[var].remove(value)

        if removals is not None:
            removals.append((var, value))

    def restore(self, removals):
        for B, b in removals:
            self.curr_domains[B].append(b)

    def first_assignment(self):
        self.init_curr_domains()

        assignment = {v: self.curr_domains[v][0]

                for v in self.variables if 1 == len(self.curr_domains[v])}

        self.numassigns = len(assignment)

        return assignment

    def goal_test(self, state):
            if state:

                assignment = dict(state)

                return (len(assignment) == len(self.variables) and all(self.num_conflicts(variables, assignment[variables], assignment) == 0 for variables in self.variables))

            else:

                return False




def AC3(csp, queue=None, removals=None):

    num_revised = 0
    revised = False
    bstr = " "


    if queue is None:
        queue = [(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]]

    csp.init_curr_domains()

    while queue:

        (Xi, Xj) = queue.pop()

        revised = revise(csp, Xi, Xj, removals)

        num_revised = num_revised + revised

        if revised:

            if not csp.curr_domains[Xi]:
                return False

            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))


    if num_revised:
        if csp.goal_test(csp.first_assignment()):

            csp.display(own="Result, Goal reached!", assignment=csp.first_assignment(), curr_domains={})

    return True


def revise(csp, Xi, Xj, removals):
    num_revised = 0

    for x in csp.curr_domains[Xi][:]:

        # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x

        if all(not csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):

            csp.prune(Xi, x, removals)

            num_revised += 1

    return num_revised




# Backtracking 
def first_unassigned_variable(assignment, csp):
    return [var for var in csp.variables if var not in assignment][0]


def mrv_degree(assignment, csp):

    mrvd_d = dict([(var, num_legal_values(csp, var, assignment)) for var in csp.variables if var not in assignment])

    mrvd_order = sorted(mrvd_d.items(), key=lambda d: d[1])

    mrvmin = mrvd_order[0][1]

    mrvdmaxvar = max([v for (v, value) in mrvd_order if value == mrvmin], key=lambda v: len(csp.neighbors[v]))



    return mrvdmaxvar

def mrv_maxtlen(assignment, csp):

    nlv_d = dict([(var, num_legal_values(csp, var, assignment)) for var in csp.variables if var not in assignment])
    nlv_order = sorted(nlv_d.items(), key = lambda d:d[1])
    mrvmin = nlv_order[0][1]
    mrvmaxtlvar = max([v for (v, value) in nlv_order if value == mrvmin], key=lambda v:csp.variables[v])

    return mrvmaxtlvar


def num_legal_values(csp, var, assignment):

    if csp.curr_domains:

        return len(csp.curr_domains[var])

    else:

        return sum(csp.num_conflicts(var, val, assignment) == 0

                     for val in csp.domains[var])


# se ordenan los valores
def unordered_domain_values(var, assignment, csp):

    return (csp.curr_domains or csp.domains)[var]


def lcv(var, assignment, csp):

    lcvorder= sorted((csp.curr_domains or csp.domains)[var],

                  key=lambda val: sum(not csp.constraints(var, val, var2, y) for var2 in csp.neighbors[var]
                                      for y in (csp.curr_domains or csp.domains)[var2]))


    return lcvorder


def minpcost(var, assignment, csp):


    minpcostorder = sorted((csp.curr_domains or csp.domains)[var],key=lambda pcost: csp.pandcs[pcost])


    return minpcostorder


# Inferencia AC3
def no_inference(csp, var, value, assignment, removals):

    return True


def mac(csp, var, value, assignment, removals):

    return AC3(csp, [(X, var) for X in csp.neighbors[var]], removals)




#busqueda backtracking
def backtracking_search(csp,select_unassigned_variable,order_domain_values,inference):

    def backtrack(assignment):

        if len(assignment) == len(csp.variables):

            return assignment

        var = select_unassigned_variable(assignment, csp)

        for value in order_domain_values(var, assignment, csp):

            if 0 == csp.num_conflicts(var, value, assignment):

                csp.assign(var, value, assignment)

                removals = csp.change_curr_domains(var, value)

                if inference(csp, var, value, assignment, removals):

                    result = backtrack(assignment)

                    if result is not None:
                        return result

                csp.undoassign(var, assignment)

                csp.restore(removals)

                csp.display(own="backtrack", assignment=assignment, curr_domains=csp.curr_domains)

        return None

    result = backtrack(csp.first_assignment())

    if csp.goal_test(result):
        csp.display(own="Result, Goal reached!", assignment=result, curr_domains={})

    else:
        print("No se encontro una solucion")
        csp.display(own="sinSolucion", assignment=result, curr_domains={})

    return result










