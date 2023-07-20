# This file is the main file of the project.
# In this file the all the functions of this project are called.

#################################################
# Import the necessary functions and packages   #
#################################################
from import_data import import_data
from model_optimize import model_optimize
from output_data import output_data
from output_function import output_function
from f_c import f_c
import time
from datetime import datetime
import numpy as np


# Start timer to record the runtime of the script
start_time = time.time()

#################################################
# Define file paths                             #
#################################################

# C:\Users\sweet\Documents\01_Daten\06_Studium\14_SS23\REXS-Modell-Matching\Sample_Data\REXS-Database\FVA_2-stage_industry-gearbox\fva_2-stage_industry-gearbox_1-2.rexsj

# Define path of the import files, must end with ".json"
input_file = "Sample_Data/REXS-Database\FVA_2-stage_industry-gearbox/fva_2-stage_industry-gearbox_1-2.rexsj" # data of the first model
input_file_prime = "Sample_Data/REXS-Database/FVA_2-stage_industry-gearbox/fva_2-stage_industry-gearbox_1-3.rexsj" # data of the second model

# Define the path and name for the output file
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"output/FVA_2-stage_industry-gearbox\/output_{current_datetime}.txt"
output_file_json = f"output/FVA_2-stage_industry-gearbox\/output_{current_datetime}.json"


# Define the role ordering of the relations
relations_roles = ["assembly", "part", "stage", "gear_1", "gear_2", "gear", "stage_gear_data", "inner_part", "outer_part", "left", "right", "origin", "referenced", "workpiece", "tool", "manufacturing_settings", "planetary_stage", "shaft", "side_1", "side_2"]


#################################################
# Import the data                               #
#################################################

components, relations = import_data(input_file, relations_roles) # components and relations of the first model
components_prime, relations_prime = import_data(input_file_prime, relations_roles) # components and relations of the second model


#################################################
# Set the parameters and functions of the model #
#################################################

f_c_matrix = f_c(components, components_prime) # distance function of the components
g_r = np.ones((len(relations), len(relations_prime))).tolist() # distance function of the relations
gamma_c = np.zeros(len(components)).tolist() # penalty for unmatched components of data model 1
gamma_c_prime = np.zeros(len(components_prime)).tolist() # penalty for unmatched components of data model 2
delta_r = np.zeros(len(relations)).tolist() # penalty for unmatched relations of data model 1
delta_r_prime = np.zeros(len(relations_prime)).tolist() # penalty for unmatched relations of data model 2
epsilon = 5 # penalty for matched components with different types

#################################################
# Optimize the model                            #
#################################################

sol_x, sol_z, objective_value  = model_optimize(components, relations, components_prime, relations_prime, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon, f_c_matrix, g_r)

# account for numerical errors
for i in range(len(sol_x)):
    for j in range(len(sol_x[0])):
        if sol_x[i][j] > 0.9999999:
            sol_x[i][j] = 1
        else:
            sol_x[i][j] = 0
for i in range(len(sol_z)):
    for j in range(len(sol_z[0])):
        if sol_z[i][j] > 0.9999999:
            sol_z[i][j] = 1
        else:
            sol_z[i][j] = 0
            
#################################################
# Output the data                               #
#################################################

output_data(sol_x, sol_z, objective_value, components, components_prime, relations, relations_prime, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon, f_c_matrix, g_r, input_file, input_file_prime, output_file)
output_function(components, components_prime, sol_x, sol_z, output_file_json)

# Stop the timer and print the time it took to run the script
end_time = time.time()
delta_time = end_time - start_time
print("This script took", time.strftime("%Hh %Mm %Ss", time.gmtime(delta_time)))
