from find_index import find_index
from pyscipopt import Model
import sys
import time


def model_optimize(components:list, relations:list, components_prime:list, relations_prime:list, gamma_c:list, gamma_c_prime:list, delta_r:list, delta_r_prime:list, epsilon, f_c, g_r, outputfile_runtime):

    start_time = time.time()
    

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
    
    end_time = time.time()
    delta_time = end_time - start_time
    line1= f"Creating the variables took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line1)
    # Define the objective function
    
    # All parts of the objective function
    start_time = time.time()
    T1 = sum(f_c[i][j] * x[i][j] for i in range(x_rows) for j in range(x_cols)) # Reward term 1 for the components
    end_time = time.time()
    delta_time = end_time - start_time
    line2= f"Preparing part T1 of the objectve function took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line2)
    start_time = time.time()
    T2 = sum(g_r[k][l] * z[k][l] for k in range(z_rows) for l in range(z_cols)) # Reward term 2 for the relations
    end_time = time.time()
    delta_time = end_time - start_time
    line3= f"Preparing part T2 of the objectve function took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line3)
    start_time = time.time()
    T3 = sum(gamma_c[i] * (1 - sum(x[i][j] for j in range(x_cols))) for i in range(x_rows)) # Penalty term for unmatched components in the first data model
    end_time = time.time()
    delta_time = end_time - start_time
    line4= f"Preparing part T3 of the objectve function took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line4)
    start_time = time.time()
    T4 = sum(gamma_c_prime[j] * (1- sum(x[i][j] for i in range(x_rows))) for j in range(x_cols)) # Penalty term for unmatched components in the second data model
    end_time = time.time()
    delta_time = end_time - start_time
    line5= f"Preparing part T4 of the objectve function took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line5)
    start_time = time.time()
    T5 = sum(delta_r[k] * (1 - sum(z[k][l] for l in range(z_cols))) for k in range(z_rows)) # Penalty terms for unmatched relations in the first data model
    end_time = time.time()
    delta_time = end_time - start_time
    line6= f"Preparing part T5 of the objectve function took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line6)
    start_time = time.time()
    T6 = sum(delta_r_prime[l] * (1 - sum(z[k][l] for k in range(z_rows))) for l in range(z_cols)) # Penalty term for unmatched relations in the second data model
    end_time = time.time()
    delta_time = end_time - start_time
    line7= f"Preparing part T6 of the objectve function took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line7)
    start_time = time.time()
    

    # Penaltyterm for matched components with different types
    T7 = 0
    for c in range(x_rows):
        for c_prime in range(x_cols):
            if components[c].type != components_prime[c_prime].type:
                T7 += epsilon *x[c][c_prime]
    end_time = time.time()
    delta_time = end_time - start_time
    line8= f"Preparing part T7 of the objectve function took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line8)
    start_time = time.time()
    # Objective as a whole
    objective = T1+T2-T3-T4-T5-T6-T7
    end_time = time.time()
    delta_time = end_time - start_time
    line9= f"Putting the objective function together took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line9)
    start_time = time.time()
    # Set the objective function
    model.setObjective(objective, sense = 'maximize')
    end_time = time.time()
    delta_time = end_time - start_time
    line10= f"Setting the objective function took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line10)
    start_time = time.time()
    
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
    

    end_time = time.time()
    delta_time = end_time - start_time
    line11= f"Preparing the constraint 1 took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line11)
    start_time = time.time()

    # Constraints (2.2), (2.3) in the thesis: one compnent can only be matched to one other component
    for c in range(x_rows):    
        model.addCons(sum(x[c][c_prime] for c_prime in range(x_cols)) <= 1)
    
    end_time = time.time()
    delta_time = end_time - start_time
    line12= f"Preparing the constraint 2 took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line12)
    start_time = time.time()

    for c_prime in range(x_cols):
        model.addCons(sum(x[c][c_prime] for c in range(x_rows)) <= 1)
    
    end_time = time.time()
    delta_time = end_time - start_time
    line13= f"Preparing the constraint 3 took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line13)
    start_time = time.time()


    # Constraints (2.4), (2.5) in the thesis: one relation can only be matched to one other relation
    for r in range(z_rows):
        model.addCons(sum(z[r][r_prime] for r_prime in range(z_cols)) <= 1)
    
    end_time = time.time()
    delta_time = end_time - start_time
    line14= f"Preparing the constraint 4 took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."  
    print(line14)
    start_time = time.time()
    
    for r_prime in range(z_cols):
        model.addCons(sum(z[r][r_prime] for r in range(z_rows)) <= 1)
    
    end_time = time.time()
    delta_time = end_time - start_time
    line15= f"Preparing the constraint 5 took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line15)
    start_time = time.time()

    # Constraints to ensure that relations are only matched if they are of the same type
    for r in range(z_rows):
        for r_prime in range(z_cols):
            if relations[r].type != relations_prime[r_prime].type:
                model.addCons(z[r][r_prime] == 0)

    end_time = time.time()
    delta_time = end_time - start_time
    line16= f"Preparing the constraint 6 took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line16)
    start_time = time.time()
    
    # Solve the model
    model.optimize()

    end_time = time.time()
    delta_time = end_time - start_time
    line17= f"Solving the model took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line17)
    start_time = time.time()
    
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

    end_time = time.time()
    delta_time = end_time - start_time
    line18= f"Getting the solution took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
    print(line18)
    
    with open(outputfile_runtime, "w") as file:
        file.write(line1)
        file.write("\n")
        file.write(line2)
        file.write("\n")
        file.write(line3)
        file.write("\n")
        file.write(line4)
        file.write("\n")
        file.write(line5)
        file.write("\n")
        file.write(line6)
        file.write("\n")
        file.write(line7)
        file.write("\n")
        file.write(line8)
        file.write("\n")
        file.write(line9)
        file.write("\n")
        file.write(line10)
        file.write("\n")
        file.write(line11)
        file.write("\n")
        file.write(line12)
        file.write("\n")
        file.write(line13)
        file.write("\n")
        file.write(line14)
        file.write("\n")
        file.write(line15)
        file.write("\n")
        file.write(line16)
        file.write("\n")
        file.write(line17)
        file.write("\n")
        file.write(line18)

    return sol_x, sol_z, obj_val