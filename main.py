# This file is the main file of the project.
# In this file all the functions of this project are called and executed.
# Executing this file will run the whole project.

#################################################
# Import the necessary functions and packages   #
#################################################
from import_data import import_data
from model_optimize import model_optimize
from output_function import output_function
from f_c import f_c
from check_unique_ids import check_unique_ids

import numpy as np
import configparser
import os


# Get the config file
config = configparser.ConfigParser()
config.read("settings.ini")

#################################################
# Define file paths                             #
#################################################

### Define path of the import files
input_file = config["InputFiles"]["input_file_A"] # Data of the model A
input_file_prime = config["InputFiles"]["input_file_B"] # Data of the model B


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

f_c_matrix = f_c(components, components_prime) # Similarity function of the components
g_r = np.ones((len(relations), len(relations_prime))) # Similarity function of the relations


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
# Check if the output folder exists and create it if it doesn't
path_exists = os.path.exists("output")
if not path_exists:
    os.makedirs("output")

output_file_json = f"output/output.json"

# Output the data
output_function(components, components_prime, sol_x, input_file, input_file_prime, output_file_json, components_unique, relations_unique, components_prime_unique, relations_prime_unique, infeasible)
