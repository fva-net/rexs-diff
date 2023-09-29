from find_index import find_index
from pyscipopt import Model


def model_optimize(components: list, relations: list, components_prime: list, relations_prime: list, f_c: list, g_r: list):
    """
    This function defines and solves  the optimization problem.\n
    Input: \n
        - components: list of components of model A.\n
        - relations: list of relations of model B.\n
        - components_prime: list of components of model B.\n
        - relations_prime: list of relations of model B.\n
        - f_c: natrix with values of the similarity function of the components as a list.\n
        - g_r: matrix with values of the similarity function of the relations as a list.\n
    Output: \n
        - sol_x: solution of the optimization problem for the components as a list.\n
        - sol_z: solution of the optimization problem for the relations as a list.\n
        - obj_val: objective value of the optimization problem as a float.\n
        - infeasible: boolean if the optimization problem is infeasible.\n
    """
    
    # Initialize the model
    model = Model()

    # Write the console output to the outputfile
    #model.setLogfile("output/log.txt")

    # Define auxiliary variables
    len_comp = len(components)
    len_comp_prime = len(components_prime)
    len_rel = len(relations)
    len_rel_prime = len(relations_prime)

    # Define the optimization variables
    x_rows = len_comp
    x_cols = len_comp_prime
    z_rows = len_rel
    z_cols = len_rel_prime

    x = [[model.addVar(vtype='BINARY') for i in range(x_cols)] for j in range(x_rows)] # Variable for each pair of components; 0 if not matched, 1 if matched
    z = [[model.addVar(vtype='BINARY') for i in range(z_cols)] for j in range(z_rows)] # Variable for each pair of relations; 0 if not matched, 1 if matched
    
   
    # Define the objective function as seperate parts
    # Reward term 1 for the components
    T1=0
    for i in range(x_rows):
        for j in range(x_cols):
            if f_c[i][j] != 0:
                T1 += f_c[i][j] * x[i][j]
    
    # Reward term 2 for the relations
    T2=0
    for k in range(z_rows):
        for l in range(z_cols):
            if g_r[k][l] != 0:
                T2 += g_r[k][l] * z[k][l]
    
    # Objective as a whole
    objective = T1+T2 

    # Set the objective function
    model.setObjective(objective, sense = 'maximize')
    
    
    # Define the constraints
    # Constraints (2.2) in the thesis: relations can only be matched if their components are also matched
    for r in relations:
        for r_prime in relations_prime:
            r_index = find_index(r.id, relations)
            r_prime_index = find_index(r_prime.id, relations_prime)
            # Only for relations that are of the same type and same order
            if r.type == r_prime.type:
                if "ordered" in r.type:
                    if r.order ==r_prime.order:
                        for i in range(len(r.refs)):
                            c_index= find_index(r.refs[i].id, components)
                            c_prime_index = find_index(r_prime.refs[i].id, components_prime)
                            model.addCons(z[r_index][r_prime_index] <= x[c_index][c_prime_index])
                    else: 
                        model.addCons(z[r_index][r_prime_index] == 0)
                else:
                    for i in range(len(r.refs)):
                        c_index= find_index(r.refs[i].id, components)
                        c_prime_index = find_index(r_prime.refs[i].id, components_prime)
                        model.addCons(z[r_index][r_prime_index] <= x[c_index][c_prime_index])                                        
            else:
                model.addCons(z[r_index][r_prime_index] == 0)
    

    # Constraints (2.3), (2.4) in the thesis: one compnent can only be matched to one other component
    for c in range(x_rows):    
        model.addCons(sum(x[c][c_prime] for c_prime in range(x_cols)) <= 1)

    for c_prime in range(x_cols):
        model.addCons(sum(x[c][c_prime] for c in range(x_rows)) <= 1)
    
    # Constraints (2.5), (2.6) in the thesis: one relation can only be matched to one other relation
    for r in range(z_rows):
        model.addCons(sum(z[r][r_prime] for r_prime in range(z_cols)) <= 1)
    
    for r_prime in range(z_cols):
        model.addCons(sum(z[r][r_prime] for r in range(z_rows)) <= 1)


    # Solve the model
    model.optimize()

    #model.writeProblem("output/model.lp")
    
    # Get the solution 
    if model.getStatus() == "optimal":             
        # Get the best solution
        obj_val = model.getObjVal()
        sol_x = [[model.getVal(x[i][j]) for j in range(x_cols)] for i in range(x_rows)]
        sol_z = [[model.getVal(z[i][j]) for j in range(z_cols)] for i in range(z_rows)]
        infeasible = False
    elif model.getStatus() == "infeasible":
        print("The model is infeasible.")
        sol_x = None
        sol_z = None
        obj_val = None
        infeasible = True
    
    return sol_x, sol_z, obj_val, infeasible