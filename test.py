
#################################################
# Import the necessary functions and packages   #
#################################################
from import_data import import_data
from model_optimize import model_optimize
from output_data import output_data
from f_c import f_c
from find_index import find_index
from output_function import output_function
from obj_func import obj_func
from which_relations import which_relations
import time
from datetime import datetime
import numpy as np


# Start timer to record the runtime of the script
start_time = time.time()

#################################################
# Define file paths                             #
#################################################
# C:\DATEN\Masterarbeit\rexs-diff\Sample_Data\REXS-Database\FVA_2-stage_industry-gearbox\fva_2-stage_industry-gearbox_1-2.rexsj

# Define path of the import files, must be a json-file
input_file = "Sample_Data/REXS-Database/FVA_Planetenstufe_Minusgetriebe/fva_planetenstufe_minusgetriebe_1-1.rexsj" # data of the first model
input_file_prime = "Sample_Data/REXS-Database/FVA_Planetenstufe_Minusgetriebe/fva_planetenstufe_minusgetriebe_1-2.rexsj" # data of the second model

# Define the path and name for the output file
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"output/output_{current_datetime}.txt"
output_file_json = f"output/output_{current_datetime}.json"



# Define the role ordering of the relations
relations_roles = ["assembly", "part", "stage", "gear_1", "gear_2", "gear", "stage_gear_data", "inner_part", "outer_part", "left", "right", "origin", "referenced", "workpiece", "tool", "manufacturing_settings", "planetary_stage", "shaft"]


#################################################
# Import the data                               #
#################################################

components, relations = import_data(input_file, relations_roles) # components and relations of the first model
components_prime, relations_prime = import_data(input_file_prime, relations_roles) # components and relations of the second model

# print(f"component, 249: {components[find_index(249, components)]}")
# print(f"component, 211: {components[find_index(211, components)]}")
# print(f"component, 212: {components[find_index(212, components)]}") 
# print(f"component, 213: {components[find_index(213, components)]}")

# print(f"component_prime, 55: {components_prime[find_index(55, components_prime)]}")
# print(f"component_prime, 211: {components_prime[find_index(211, components_prime)]}")
# print(f"component_prime, 212: {components_prime[find_index(212, components_prime)]}")
# print(f"component_prime, 213: {components_prime[find_index(213, components_prime)]}")

# print(f"relations, 257: {relations[find_index(257, relations)]}")
print(f"relations_prime, 127: {relations_prime[find_index(127, relations_prime)]}")

id = 56
print(f"Component {id} is in relations {which_relations(id, relations_prime)}")

# Set the parameters and functions of the model #
#################################################



f_c_matrix = f_c(components, components_prime) # distance function of the components
# g_r = np.ones((len(relations), len(relations_prime))).tolist() # distance function of the relations
# gamma_c = np.zeros(len(components)).tolist() # penalty for unmatched components of data model 1
# gamma_c_prime = np.zeros(len(components_prime)).tolist() # penalty for unmatched components of data model 2
# delta_r = np.zeros(len(relations)).tolist() # penalty for unmatched relations of data model 1
# delta_r_prime = np.zeros(len(relations_prime)).tolist() # penalty for unmatched relations of data model 2
# epsilon = 5 # penalty for matched components with different types

# id= 228
# id_prime = 33
# f= f_c_matrix[find_index(id, components)][find_index(id_prime, components_prime)]
# print(f)


#################################################
# Objective function                            #
#################################################

# objective_value = obj_func(components, components_prime, relations, relations_prime, f_c_matrix, g_r, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon)

# print(objective_valsue)

#################################################
# Optimize the model                            #
#################################################

# sol_x, sol_z, objective_value  = model_optimize(components, relations, components_prime, relations_prime, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon, f_c_matrix, g_r)


#################################################
# Output the data                               #
#################################################

# output_function(components, components_prime, sol_x, sol_z, output_file_json)


# output_data(sol_x, sol_z, objective_value, components, components_prime, relations, relations_prime, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon, f_c_matrix, g_r, input_file, input_file_prime, output_file)
# wrong_matches(sol_x, sol_z, components, relations, components_prime, relations_prime)

# Stop the timer and print the time it took to run the script
end_time = time.time()
delta_time = end_time - start_time
print("This script took", time.strftime("%Hh %Mm %Ss", time.gmtime(delta_time)))
