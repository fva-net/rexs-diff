
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
from check_unique_ids import check_unique_ids
import time
from datetime import datetime
import numpy as np
import os


# Start timer to record the runtime of the script
start_time = time.time()

#################################################
# Define file paths                             #
#################################################


# Define path of the import files, must be a json-file
input_file = "Sample_Data/REXS-Database/FVA_Planetenstufe_Minusgetriebe/fva_planetenstufe_minusgetriebe_1-4.rexsj" # data of the first model
input_file_prime = "Sample_Data/REXS-Database/FVA_Planetenstufe_Minusgetriebe/fva_planetenstufe_minusgetriebe_1-4_export.rexsj" # data of the second model


# Define the path and name for the output file
# current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# foldername = "BEARINX_37_LKW-Planetengetriebe" # change this to the name of the folder you want to save the output files in

# Check if the folder exists and create it if it doesn't
# path_exists = os.path.exists(f"output/{foldername}")
# if not path_exists:
#     os.makedirs(f"output/{foldername}")

# Output files paths
# os.makedirs(f"output/{foldername}/{current_datetime}_test")

# output_file = f"output/{foldername}/{current_datetime}_test/{current_datetime}_output.txt"
# output_file_json = f"output/{foldername}/{current_datetime}_test/{current_datetime}_output.json"
# output_file_runtime = f"output/{foldername}/{current_datetime}_test/{current_datetime}_runtime.txt"




# Define the role ordering of the relations
relations_roles = ["assembly", "part", "stage", "gear_1", "gear_2", "gear", "stage_gear_data", "inner_part", "outer_part", "left", "right", "origin", "referenced", "workpiece", "tool", "manufacturing_settings", "planetary_stage", "shaft"]


#################################################
# Import the data                               #
#################################################

components, relations = import_data(input_file, relations_roles) # components and relations of the first model
components_prime, relations_prime = import_data(input_file_prime, relations_roles) # components and relations of the second model

# Check for double IDs in the components and relations
components_unique, components_double = check_unique_ids(components, "component")
relations_unique, relations_double = check_unique_ids(relations, "relation")
components_prime_unique, components_prime_double = check_unique_ids(components_prime, "component")
relations_prime_unique, relations_prime_double = check_unique_ids(relations_prime, "relation")

if components_unique == False:
    print(f"ERRORR: The IDs of the components in {input_file} are not unique. \n The non-unique IDs are: {components_double}")

if relations_unique == False:
    print(f"ERRORR: The IDs of the relations in {input_file} are not unique. \n The non-unique IDs are: {relations_double}")

if components_prime_unique == False:
    print(f"ERRORR: The IDs of the components in {input_file_prime} are not unique. \n The non-unique IDs are: {components_prime_double}")

if relations_prime_unique == False:
    print(f"ERRORR: The IDs of the relations in {input_file_prime} are not unique. \n The non-unique IDs are: {relations_prime_double}")

if components_unique == False or relations_unique == False or components_prime_unique == False or relations_prime_unique == False:
    print("Please fix the non-unique IDs and try again.")
    exit()


print(f"component, 36: {components[find_index(36, components)]}")
# print(f"component, 91: {components[find_index(91, components)]}")
# print(f"component, 212: {components[find_index(212, components)]}") 
# print(f"component, 213: {components[find_index(213, components)]}")

# print(f"component_prime, 36: {components_prime[find_index(36, components_prime)]}")
# print(f"component_prime, 91: {components_prime[find_index(91, components_prime)]}")
# print(f"component_prime, 212: {components_prime[find_index(212, components_prime)]}")
# print(f"component_prime, 213: {components_prime[find_index(213, components_prime)]}")

# print(f"relations, 178: {relations[find_index(178, relations)]}")
# print(f"relations_prime, 269: {relations_prime[find_index(269, relations_prime)]}")

# id = 1880
# print(f"Component {id} is in relations {which_relations(id, relations_prime)}")

#################################################
# Set the parameters and functions of the model #
#################################################



# f_c_matrix = f_c(components, components_prime) # distance function of the components
# g_r = np.ones((len(relations), len(relations_prime))) # distance function of the relations
# gamma_c = np.zeros(len(components)) # penalty for unmatched components of data model 1
# gamma_c_prime = np.zeros(len(components_prime)) # penalty for unmatched components of data model 2
# delta_r = np.zeros(len(relations)) # penalty for unmatched relations of data model 1
# delta_r_prime = np.zeros(len(relations_prime)) # penalty for unmatched relations of data model 2
# epsilon = 5 # penalty for matched components with different types

# id= 91
# id_prime = 91
# f= f_c_matrix[find_index(id, components)][find_index(id_prime, components_prime)]
# print(f"The similarity of component {id} and component {id_prime} is {f}")
# id_rel= 178
# id_prime_rel = 269
# g= g_r[find_index(id_rel, relations)][find_index(id_prime_rel, relations_prime)]
# print(f"The similarity of relation {id_rel} and relation {id_prime_rel} is {g}")

#################################################
# Objective function                            #
#################################################

# objective_value = obj_func(components, components_prime, relations, relations_prime, f_c_matrix, g_r, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon)

# print(objective_value)

#################################################
# Optimize the model                            #
#################################################

# sol_x, sol_z, objective_value  = model_optimize(components, relations, components_prime, relations_prime, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon, f_c_matrix, g_r, outputfile_runtime = "output/Tests/output_file_runtime.txt")


#################################################
# Output the data                               #
#################################################
# id =128
# id_prime = 208
# id_rel = 247
# id_prime_rel = 339

# print(f"sol_x[{id}][{id_prime}] = {sol_x[find_index(id, components)][find_index(id_prime, components_prime)]}")
# print(f"sol_z[{id_rel}][{id_prime_rel}] = {sol_z[find_index(id_rel, relations)][find_index(id_prime_rel, relations_prime)]}")

# # output_function(components, components_prime, sol_x, sol_z, output_file_json)


# output_data(sol_x, sol_z, objective_value, components, components_prime, relations, relations_prime, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon, f_c_matrix, g_r, input_file, input_file_prime, output_file)
# # wrong_matches(sol_x, sol_z, components, relations, components_prime, relations_prime)

# # Stop the timer and print the time it took to run the script
# end_time = time.time()
# delta_time = end_time - start_time
# print("This script took", time.strftime("%Hh %Mm %Ss", time.gmtime(delta_time)))
