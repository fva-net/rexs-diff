# This file is the main file of the project.
# In this file all the functions of this project are called and executed.
# Executing this file will run the whole project.

#################################################
# Import the necessary functions and packages   #
#################################################
from sys import stdout
from import_data import import_data
from model_optimize import model_optimize
from output_function import output_function
from f_c import f_c
from check_unique_ids import check_unique_ids

from np_ones_zeros_math import ones
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--modelA","-a", type=str, required=True)
parser.add_argument("--modelB", "-b", type=str, required=True)
parser.add_argument("--relative_tol", type=float, required=False)
parser.add_argument("--absolute_tol", type=float, required=False)
parser.add_argument("--check_both_tol", "-c", default=False, action='store_true')
args = parser.parse_args()
# if args.help:
    # print("This is the helptext: \nKnown Arguments: ") # TODO 
    

#################################################
# Define file paths                             #
#################################################
### Define path of the import files
# input_file = "C:\\diff.rexsj" #args.modelA
# input_file_prime = "C:\\diff2.rexsj" #args.modelB
# absolute_tol = 2 #args.absolute_tol
# relative_tol = 2 #args.relative_tol
# check_both_tol = True #args.check_both_tol

input_file = args.modelA
input_file_prime = args.modelB
absolute_tol = args.absolute_tol
relative_tol = args.relative_tol
check_both_tol = args.check_both_tol

#################################################
# Import the data                               #
#################################################

components, relations = import_data(input_file) # Components and relations of model A
components_prime, relations_prime = import_data(input_file_prime) # Components and relations of model B


#################################################
# Check for non unique IDs                      #
#################################################

components_unique = check_unique_ids(components)
relations_unique = check_unique_ids(relations)
components_prime_unique = check_unique_ids(components_prime)
relations_prime_unique = check_unique_ids(relations_prime)


##############################################################
# Set the parameters and functions of the optimization model #
##############################################################

f_c_matrix = f_c(components, components_prime, absolute_tol, relative_tol, check_both_tol) # Similarity function of the components
g_r = ones(len(relations), len(relations_prime)) # Similarity function of the relations


#################################################
# Optimize the model                            #
#################################################

sol_x, sol_z, objective_value, infeasible = model_optimize(components, relations, components_prime, relations_prime, f_c_matrix, g_r)

# account for numerical errors
if infeasible == False:
    for i in range(len(sol_x)):
        for j in range(len(sol_x[0])):
            if sol_x[i][j] > 0.5:
                sol_x[i][j] = 1
            else:
                sol_x[i][j] = 0
    for i in range(len(sol_z)):
        for j in range(len(sol_z[0])):
            if sol_z[i][j] > 0.5:
                sol_z[i][j] = 1
            else:
                sol_z[i][j] = 0

            
#################################################
# Output the data                               #
#################################################

# Outputfile path
# mit Sarah absprechen: (-> ins stdout) -> Readme anpassen 
# output_file_json = f"output/output.json"

# Output the data
output_function(components, components_prime, sol_x, input_file, input_file_prime, stdout, components_unique, relations_unique, components_prime_unique, relations_prime_unique, infeasible, absolute_tol, relative_tol, check_both_tol)
