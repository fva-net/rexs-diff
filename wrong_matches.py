import os
def wrong_matches(sol_x, sol_z, components, relations, components_prime, relations_prime):
    
    with open("output/output_wrong.txt", "w") as file:
        file.write("The wrongly matched components are: \n")
        for i in range(len(sol_x)):
            for j in range(len(sol_x[0])):
                if sol_x[i][j]==1:
                    if components[i].id != components_prime[j].id:
                        file.write(f"{components[i].id} | {components_prime[j].id} \n")
        file.write("\n")
        file.write("The wrongly matched relations are: \n")
        for i in range(len(sol_z)):
            for j in range(len(sol_z[0])):
                if sol_z[i][j]==1:
                    if relations[i].id != relations_prime[j].id:
                        file.write(f"{relations[i].id} | {relations_prime[j].id} \n")

    os.remove("output/log.txt")
    os.remove("output/model.lp")
    os.remove("output/solutions.txt")