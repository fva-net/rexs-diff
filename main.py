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
from check_unique_ids import check_unique_ids

from datetime import datetime
import numpy as np
import os
import configparser



# Get the config file
config = configparser.ConfigParser()
config.read("settings.ini")

#################################################
# Define file paths                             #
#################################################

### Define path of the import files
input_file = config["InputFiles"]["input_file_1"] # data of the model A
input_file_prime = config["InputFiles"]["input_file_2"] # data of the model B

### Define the path and name for the output file
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
outputfolder = config["OutputFiles"]["output_dir"] # name of the folder to save the output files in

# Check if the folder exists and create it if it does not
path_exists = os.path.exists(outputfolder)
if not path_exists:
    os.makedirs(outputfolder)

# Define/Create folder for output file
os.makedirs(f"{outputfolder}/{current_datetime}")

output_file_json = f"{outputfolder}/{current_datetime}/{current_datetime}_output.json"



### Define the role ordering of the relations
relations_roles = ["assembly", "part", "stage", "gear_1", "gear_2", "gear", "stage_gear_data", "inner_part", "outer_part", "left", "right", "origin", "referenced", "workpiece", "tool", "manufacturing_settings", "planetary_stage", "shaft", "side_1", "side_2"]


#################################################
# Import the data                               #
#################################################

components, relations = import_data(input_file, relations_roles) # components and relations of the first model
components_prime, relations_prime = import_data(input_file_prime, relations_roles) # components and relations of the second model


#################################################
# Check for non unique IDs                      #
#################################################

components_unique = check_unique_ids(components)
relations_unique = check_unique_ids(relations)
components_prime_unique = check_unique_ids(components_prime)
relations_prime_unique = check_unique_ids(relations_prime)


#################################################
# Set the parameters and functions of the model #
#################################################

f_c_matrix = f_c(components, components_prime) # similarity function of the components
g_r = np.ones((len(relations), len(relations_prime))) # similarity function of the relations


#################################################
# Optimize the model                            #
#################################################

sol_x, sol_z, objective_value = model_optimize(components, relations, components_prime, relations_prime, f_c_matrix, g_r)


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

# Outputfile path
# TODO: mit Sarah: wohin abspeichern?
output_file_json = f"output/{outputfolder}/{current_datetime}/{current_datetime}_output.json"

# Output the data
output_function(components, components_prime, sol_x, sol_z, input_file, input_file_prime, output_file_json, components_unique, relations_unique, components_prime_unique, relations_prime_unique)

