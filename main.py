# This file is the main file of the project.
# In this file the all the functions of this project are called and executed.

#################################################
# Import the necessary functions and packages   #
#################################################
from import_data import import_data
from model_optimize import model_optimize
from output_data import output_data
from output_function import output_function
from f_c import f_c
from add_runtime import add_runtime
from check_unique_ids import check_unique_ids

import time
from datetime import datetime
import numpy as np
import os
import configparser


# Start timer to record the runtime of the script
start_time = time.time()
start_time_script = time.time()
print("Test")
# Get the config file
config = configparser.ConfigParser()
config.read("settings.ini")

#################################################
# Define file paths                             #
#################################################

### Define path of the import files
input_file = config["InputFiles"]["input_file_1"] # data of the first model
input_file_prime = config["InputFiles"]["input_file_2"] # data of the second model

### Define the path and name for the output file
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
outputfolder = config["OutputFiles"]["output_dir"] #name of the folder to save the output files in

# Check if the folder exists and create it if it doesn't
path_exists = os.path.exists(outputfolder)
if not path_exists:
    os.makedirs(outputfolder)

# Output files paths
os.makedirs(f"{outputfolder}/{current_datetime}")

output_file = f"{outputfolder}/{current_datetime}/{current_datetime}_output.txt"
output_file_json = f"{outputfolder}/{current_datetime}/{current_datetime}_output.json"
output_file_runtime = f"{outputfolder}/{current_datetime}/{current_datetime}_runtime.txt"


### Define the role ordering of the relations
relations_roles = ["assembly", "part", "stage", "gear_1", "gear_2", "gear", "stage_gear_data", "inner_part", "outer_part", "left", "right", "origin", "referenced", "workpiece", "tool", "manufacturing_settings", "planetary_stage", "shaft", "side_1", "side_2"]


#################################################
# Import the data                               #
#################################################

components, relations = import_data(input_file, relations_roles) # components and relations of the first model
components_prime, relations_prime = import_data(input_file_prime, relations_roles) # components and relations of the second model

end_time = time.time()
delta_time = end_time - start_time
line1=f"Importing the data took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))}."
print(line1)
start_time = time.time()

#################################################
# Check for double IDs                          #
#################################################

components_unique, components_double = check_unique_ids(components, "component")
relations_unique, relations_double = check_unique_ids(relations, "relation")
components_prime_unique, components_prime_double = check_unique_ids(components_prime, "component")
relations_prime_unique, relations_prime_double = check_unique_ids(relations_prime, "relation")

if components_unique == False:
    print(f"WARNING: The IDs of the components in {input_file} are not unique. \n The non-unique IDs are: {components_double}")

if relations_unique == False:
    print(f"WARNING: The IDs of the relations in {input_file} are not unique. \n The non-unique IDs are: {relations_double}")

if components_prime_unique == False:
    print(f"WARNING: The IDs of the components in {input_file_prime} are not unique. \n The non-unique IDs are: {components_prime_double}")

if relations_prime_unique == False:
    print(f"WARNING: The IDs of the relations in {input_file_prime} are not unique. \n The non-unique IDs are: {relations_prime_double}")

if components_unique == False or relations_unique == False or components_prime_unique == False or relations_prime_unique == False:
    print("Please fix the non-unique IDs and try again.")
    # exit()

end_time = time.time()
delta_time = end_time - start_time
line1_5=f"Checking if the IDs are unique took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))}."
print(line1_5)
start_time = time.time()

#################################################
# Set the parameters and functions of the model #
#################################################

f_c_matrix = f_c(components, components_prime) # distance function of the components
g_r = np.ones((len(relations), len(relations_prime))) # distance function of the relations
gamma_c = np.zeros(len(components)) # penalty for unmatched components of data model 1
gamma_c_prime = np.zeros(len(components_prime)) # penalty for unmatched components of data model 2
delta_r = np.zeros(len(relations)) # penalty for unmatched relations of data model 1
delta_r_prime = np.zeros(len(relations_prime)) # penalty for unmatched relations of data model 2
epsilon = 0 # penalty for matched components with different types


end_time = time.time()
delta_time = end_time - start_time
line2=f"Setting the parameters and functions of the model took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))}."
print(line2)
start_time = time.time()

#################################################
# Optimize the model                            #
#################################################

sol_x, sol_z, objective_value  = model_optimize(components, relations, components_prime, relations_prime, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon, f_c_matrix, g_r, output_file_runtime)

end_time = time.time()
delta_time = end_time - start_time
line3=f"Optimizing the model took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))}."
print(line3)
start_time = time.time()

# account for numerical errors
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

# TODO: at the end, alles aufräumen für die Abgabe
# # Outputfile path
# output_file_json = f"output/{outputfolder}/{current_datetime}/{current_datetime}_output.json"


output_data(sol_x, sol_z, objective_value, components, components_prime, relations, relations_prime, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon, f_c_matrix, g_r, input_file, input_file_prime, output_file)
output_function(components, components_prime, sol_x, sol_z, input_file, input_file_prime, output_file_json, components_unique, relations_unique, components_prime_unique, relations_prime_unique)

end_time = time.time()
delta_time = end_time - start_time
line4=f"Outputting the data took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))}."
print(line4)

# Stop the timer and print the time it took to run the script
end_time = time.time()
delta_time = end_time - start_time_script
line5=f"The script took {time.strftime('%Hh %Mm %Ss', time.gmtime(delta_time))} to run."
print(line5)

with open(output_file_runtime, "a") as file:
    file.write("\n")
    file.write(line3)
    file.write("\n")
    file.write(line4)
    file.write("\n")
add_runtime(output_file_runtime, line5, line1, line1_5, line2)
