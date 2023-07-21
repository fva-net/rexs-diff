from find_index import find_index
from pyscipopt import Model
import sys


def model_optimize(components:list, relations:list, components_prime:list, relations_prime:list, gamma_c:list, gamma_c_prime:list, delta_r:list, delta_r_prime:list, epsilon, f_c, g_r):


    model = Model()

    # Write the console output to the outputfile
    model.setLogfile("output/log.txt")

    # Define auxiliary variables
    len_comp = len(components)
    len_comp_prime = len(components_prime)
    len_rel = len(relations)
    len_rel_prime = len(relations_prime)

    # Define the variables
    x_rows = len_comp
    x_cols = len_comp_prime
    z_rows = len_rel
    z_cols = len_rel_prime

    x = [[model.addVar(vtype='BINARY') for i in range(x_cols)] for j in range(x_rows)] # Variable for each pair of components; 0 if not matched, 1 if matched
    z = [[model.addVar(vtype='BINARY') for i in range(z_cols)] for j in range(z_rows)] # Variable for each pair of relations; 0 if not matched, 1 if matched
    
    print("Preparing the optimization problem...")
    # Define the objective function
    
    # All parts of the objective function
    T1 = sum(f_c[i][j] * x[i][j] for i in range(x_rows) for j in range(x_cols)) # Reward term 1 for the components
    print("Preparing the optimization problem...")
    T2 = sum(g_r[k][l] * z[k][l] for k in range(z_rows) for l in range(z_cols)) # Reward term 2 for the relations
    print("Preparing the optimization problem...")
    T3 = sum(gamma_c[i] * (1 - sum(x[i][j] for j in range(x_cols))) for i in range(x_rows)) # Penalty term for unmatched components in the first data model
    print("Preparing the optimization problem...")
    T4 = sum(gamma_c_prime[j] * (1- sum(x[i][j] for i in range(x_rows))) for j in range(x_cols)) # Penalty term for unmatched components in the second data model
    print("Preparing the optimization problem...")
    T5 = sum(delta_r[k] * (1 - sum(z[k][l] for l in range(z_cols))) for k in range(z_rows)) # Penalty terms for unmatched relations in the first data model
    print("Preparing the optimization problem...")
    T6 = sum(delta_r_prime[l] * (1 - sum(z[k][l] for k in range(z_rows))) for l in range(z_cols)) # Penalty term for unmatched relations in the second data model
    print("Preparing the optimization problem...")
    

    # Penaltyterm for matched components with different types
    T7 = 0
    for c in range(x_rows):
        for c_prime in range(x_cols):
            if components[c].type != components_prime[c_prime].type:
                T7 += epsilon *x[c][c_prime]

    # Objective as a whole
    objective = T1+T2-T3-T4-T5-T6-T7

    # Set the objective function
    model.setObjective(objective, sense = 'maximize')


    print("Preparing the optimization problem...")

    # Define the constraints
    # Constraints (2.1) in the thesis: relations can only be matched if their components are also matched
    for r in relations:
        for r_prime in relations_prime:
            # Only for relations that are of the same type and same order
            if r.type == r_prime.type:
                if "ordered" in r.type:
                    if r.order ==r_prime.order:
                        for i in range(len(r.refs)):
                            c_index= find_index(r.refs[i].id, components)
                            c_prime_index = find_index(r_prime.refs[i].id, components_prime)
                            r_index = find_index(r.id, relations)
                            r_prime_index = find_index(r_prime.id, relations_prime)
                            model.addCons(z[r_index][r_prime_index] <= x[c_index][c_prime_index])
                    else: 
                        r_index = find_index(r.id, relations)
                        r_prime_index = find_index(r_prime.id, relations_prime)
                        model.addCons(z[r_index][r_prime_index] == 0)
                else:
                    for i in range(len(r.refs)):
                        c_index= find_index(r.refs[i].id, components)
                        c_prime_index = find_index(r_prime.refs[i].id, components_prime)
                        r_index = find_index(r.id, relations)
                        r_prime_index = find_index(r_prime.id, relations_prime)
                        model.addCons(z[r_index][r_prime_index] <= x[c_index][c_prime_index])
                                        
            else:
                r_index = find_index(r.id, relations)
                r_prime_index = find_index(r_prime.id, relations_prime)
                model.addCons(z[r_index][r_prime_index] == 0)
    

    print("Preparing the optimization problem...")

    # Constraints (2.2), (2.3) in the thesis: one compnent can only be matched to one other component
    for c in range(x_rows):    
        model.addCons(sum(x[c][c_prime] for c_prime in range(x_cols)) <= 1)
    
    print("Preparing the optimization problem...")

    for c_prime in range(x_cols):
        model.addCons(sum(x[c][c_prime] for c in range(x_rows)) <= 1)
    
    print("Preparing the optimization problem...")

    # Constraints (2.4), (2.5) in the thesis: one relation can only be matched to one other relation
    for r in range(z_rows):
        model.addCons(sum(z[r][r_prime] for r_prime in range(z_cols)) <= 1)
    
    print("Preparing the optimization problem...")
    
    for r_prime in range(z_cols):
        model.addCons(sum(z[r][r_prime] for r in range(z_rows)) <= 1)
    
    print("Preparing the optimization problem...")

    # Constraints to ensure that relations are only matched if they are of the same type
    for r in range(z_rows):
        for r_prime in range(z_cols):
            if relations[r].type != relations_prime[r_prime].type:
                model.addCons(z[r][r_prime] == 0)

    print("Preparing the optimization problem...")
    
    # Solve the model
    model.optimize()

    
    #model.writeProblem("output/model.lp")
    

    if model.getStatus() == "optimal":

        # Get the number of solutions found
        solutions = model.getSols()
        original_stdout = sys.stdout
        sys.stdout = open("output/solutions.txt", "w")
        print(solutions)
        sys.stdout= original_stdout
              

        # Get the best solution
        sol = model.getBestSol()
        obj_val = model.getObjVal()
        sol_x = [[model.getVal(x[i][j]) for j in range(x_cols)] for i in range(x_rows)]
        sol_z = [[model.getVal(z[i][j]) for j in range(z_cols)] for i in range(z_rows)]
    elif model.getStatus() == "infeasible":
        print("The model is infeasible.")


    return sol_x, sol_z, obj_val