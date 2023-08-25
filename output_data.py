import os
from find_index import find_index

def output_data(sol_x:list, sol_z:list, obj_val:list, components:list, components_prime:list, relations:list, relations_prime:list, gamma_c:list, gamma_c_prime:list, delta_r:list, delta_r_prime:list, epsilon: float, f_c: list, g_r: list,input_file: str, input_file_prime: str, outputfile: str, log_file="output/log.txt"):
    """
    This restructures the output of the optimization model to a more readable format.
    """

    # Write the output to the outputfile
    with open(outputfile, "a") as file:
        file.write(f"We have attempted to match the data in {input_file} to the data in {input_file_prime}. \n")
        # Add how many coponents and relations were matched
        components_matched=0 
        relations_matched=0
        for i in range(len(sol_x)):
            for j in range(len(sol_x[0])):
                if sol_x[i][j]==1:
                    components_matched+=1
        for i in range(len(sol_z)):
            for j in range(len(sol_z[0])):
                if sol_z[i][j]==1:
                    relations_matched+=1
        file.write(f"{components_matched}/{len(components)} components and {relations_matched}/{len(relations)} relations from the first data model were matched. \n")
        file.write(f"{components_matched}/{len(components_prime)} components and {relations_matched}/{len(relations_prime)} relations from the second data model were matched. \n \n \n")
        file.write("The following matching of components and relations was poduced: \n")
        file.write("Components are matched as follows: \n")
        table_components=[["ID", "Type", "|", "ID", "Type"]]
        for i in range(len(sol_x)):
            for j in range(len(sol_x[0])):
                if sol_x[i][j]==1:
                    id = str(components[i].id)
                    type = components[i].type
                    id_prime = str(components_prime[j].id)
                    type_prime = components_prime[j].type
                    list_components=[id, type, "|", id_prime, type_prime]
                    table_components.append(list_components)
        # Add table of matched components
        column_widths = [max(len(str(item)) for item in column) for column in zip(*table_components)]
        header_components = table_components[0]
        formatted_header = "\t".join("{{:<{}}}".format(width) for width in column_widths).format(*header_components)
        file.write(formatted_header + "\n")
        for row in table_components[1:]:
            formatted_row = "\t".join("{{:<{}}}".format(width).format(item) for width, item in zip(column_widths, row))
            file.write(formatted_row + "\n")

        file.write("\n")
        file.write("\n")
        # unmatched components
        # Data model 1
        file.write("The unmatched components from the first data model are: \n")
        table_components=[["ID", "Type"]]
        for i in range(len(sol_x)):
            match_found = False
            for j in range(len(sol_x[0])):
                if sol_x[i][j]==1:
                    match_found = True
                    break
            if not match_found:
                id = str(components[i].id)
                type = components[i].type
                list_components=[id, type]
                table_components.append(list_components)
        # Add table of unmatched components
        column_widths = [max(len(str(item)) for item in column) for column in zip(*table_components)]
        header_components = table_components[0]
        formatted_header = "\t".join("{{:<{}}}".format(width) for width in column_widths).format(*header_components)
        file.write(formatted_header + "\n")
        for row in table_components[1:]:
            formatted_row = "\t".join("{{:<{}}}".format(width).format(item) for width, item in zip(column_widths, row))
            file.write(formatted_row + "\n")

        file.write("\n")
        file.write("\n")
        # Data model 2
        file.write("The unmatched components from the second data model are: \n")
        table_components_prime=[["ID", "Type"]]
        for j in range(len(sol_x[0])):
            match_found = False
            for i in range(len(sol_x)):
                if sol_x[i][j]==1:
                    match_found = True
                    break
            if not match_found:
                id = str(components_prime[j].id)
                type = components_prime[j].type
                list_components_prime=[id, type]
                table_components_prime.append(list_components_prime)
        # Add table of unmatched components
        column_widths = [max(len(str(item)) for item in column) for column in zip(*table_components_prime)]
        header_components_prime = table_components_prime[0]
        formatted_header = "\t".join("{{:<{}}}".format(width) for width in column_widths).format(*header_components_prime)
        file.write(formatted_header + "\n")
        for row in table_components_prime[1:]:
            formatted_row = "\t".join("{{:<{}}}".format(width).format(item) for width, item in zip(column_widths, row))
            file.write(formatted_row + "\n")
        
        # Matched relations
        file.write("\n")
        file.write("Relations are matched as follows: \n")
        table_relations=[["Rel_ID", "Rel_Type", "Order", "Ref 1", "Ref 2", "Ref 3", "|","Rel_ID", "Rel_Type", "Order", "Ref 1", "Ref 2", "Ref 3"]]
        for i in range(len(sol_z)):
            for j in range(len(sol_z[0])):
                if sol_z[i][j]==1:
                    id = str(relations[i].id)
                    type = relations[i].type
                    order = relations[i].order
                    if order == None:
                        order = ""
                    refs = relations[i].refs
                    ref_1 = [str(refs[0].id), str(components[find_index(refs[0].id, components)].type)]
                    ref_2 = [str(refs[1].id), str(components[find_index(refs[1].id, components)].type)]
                    if len(refs) == 3:
                        ref_3 = [str(refs[2].id), str(components[find_index(refs[2].id, components)].type)]
                    else:
                        ref_3 = [""]
                    ref_1 = ",".join(ref_1)
                    ref_2 = ",".join(ref_2)
                    ref_3 = ",".join(ref_3)
                    # Data from the second data model
                    id_prime = str(relations_prime[j].id)
                    type_prime = relations_prime[j].type
                    order_prime = relations_prime[j].order
                    if order_prime == None:
                        order_prime = ""
                    refs_prime = relations_prime[j].refs
                    ref_1_prime = [str(refs_prime[0].id), str(components_prime[find_index(refs_prime[0].id, components_prime)].type)]
                    ref_2_prime = [str(refs_prime[1].id), str(components_prime[find_index(refs_prime[1].id, components_prime)].type)]
                    if len(refs_prime) == 3:
                        ref_3_prime = [str(refs_prime[2].id), str(components_prime[find_index(refs_prime[2].id, components_prime)].type)]
                    else:
                        ref_3_prime = [""]
                    ref_1_prime = ",".join(ref_1_prime)
                    ref_2_prime = ",".join(ref_2_prime)
                    ref_3_prime = ",".join(ref_3_prime)
                    list_relations=[id, type, order, ref_1, ref_2, ref_3,"|", id_prime, type_prime, order_prime, ref_1_prime, ref_2_prime, ref_3_prime]
                    table_relations.append(list_relations)
        # Add table of matched relations
        column_widths = [max(len(str(item)) for item in column) for column in zip(*table_relations)]
        header_relations = table_relations[0]
        formatted_header = "\t".join("{{:<{}}}".format(width) for width in column_widths).format(*header_relations)
        file.write(formatted_header + "\n")
        for row in table_relations[1:]:
            formatted_row = "\t".join("{{:<{}}}".format(width).format(item) for width, item in zip(column_widths, row))
            file.write(formatted_row + "\n")

        file.write("\n \n")    
        # unmatched relations
        # Data model 1
        file.write("The unmatched relations from the first data model are: \n")
        table_relations=[["Rel_ID", "Rel_Type", "Order", "Ref 1", "Ref 2", "Ref 3"]]
        for i in range(len(sol_z)):
            match_found = False
            for j in range(len(sol_z[0])):
                if sol_z[i][j]==1:
                    match_found = True
                    break
            if not match_found:
                id = str(relations[i].id)
                type = relations[i].type
                order = relations[i].order
                if order == None:
                    order = ""
                refs = relations[i].refs
                ref_1 = [str(refs[0].id), str(components[find_index(refs[0].id, components)].type)]
                ref_2 = [str(refs[1].id), str(components[find_index(refs[1].id, components)].type)]
                if len(refs) == 3:
                    ref_3 = [str(refs[2].id), str(components[find_index(refs[2].id, components)].type)]
                else:
                    ref_3 = [""]
                ref_1 = ",".join(ref_1)
                ref_2 = ",".join(ref_2)
                ref_3 = ",".join(ref_3)
                list_relations=[id, type, order, ref_1, ref_2, ref_3]
                table_relations.append(list_relations)
        
        # Add table of unmatched relations
        column_widths = [max(len(str(item)) for item in column) for column in zip(*table_relations)]
        header_relations = table_relations[0]
        formatted_header = "\t".join("{{:<{}}}".format(width) for width in column_widths).format(*header_relations)
        file.write(formatted_header + "\n")
        for row in table_relations[1:]:
            formatted_row = "\t".join("{{:<{}}}".format(width).format(item) for width, item in zip(column_widths, row))
            file.write(formatted_row + "\n")

        file.write("\n \n")

        # Data model 2
        file.write("The unmatched relations from the second data model are: \n")
        table_relations_prime=[["Rel_ID", "Rel_Type", "Order", "Ref 1", "Ref 2", "Ref 3"]]
        for j in range(len(sol_z[0])):
            match_found = False
            for i in range(len(sol_z)):
                if sol_z[i][j]==1:
                    match_found = True
                    break
            if not match_found:
                id = str(relations_prime[j].id)
                type = relations_prime[j].type
                order = relations_prime[j].order
                if order == None:
                    order = ""
                refs = relations_prime[j].refs
                ref_1 = [str(refs[0].id), str(components_prime[find_index(refs[0].id, components_prime)].type)]
                ref_2 = [str(refs[1].id), str(components_prime[find_index(refs[1].id, components_prime)].type)]
                if len(refs) == 3:
                    ref_3 = [str(refs[2].id), str(components_prime[find_index(refs[2].id, components_prime)].type)]
                else:
                    ref_3 = [""]
                ref_1 = ",".join(ref_1)
                ref_2 = ",".join(ref_2)
                ref_3 = ",".join(ref_3)
                list_relations_prime=[id, type, order, ref_1, ref_2, ref_3]
                table_relations_prime.append(list_relations_prime)

        # Add table of unmatched relations
        column_widths = [max(len(str(item)) for item in column) for column in zip(*table_relations_prime)]
        header_relations_prime = table_relations_prime[0]
        formatted_header = "\t".join("{{:<{}}}".format(width) for width in column_widths).format(*header_relations_prime)
        file.write(formatted_header + "\n")
        for row in table_relations_prime[1:]:
            formatted_row = "\t".join("{{:<{}}}".format(width).format(item) for width, item in zip(column_widths, row))
            file.write(formatted_row + "\n")
            
        file.write("\n \n")
        # Add the console output to the outputfile
        file.write("ScipOpt has produced the following output: \n")
        with open(log_file, "r") as f:
            log = f.read()
        file.write(log + "\n")
        file.write(f"The objective value of the optimization model is: {obj_val} \n")
        file.write("\n \n")
        file.write("The parameters and functions were set to the following values: \n")
        file.write(f"f_c: {f_c.tolist()} \n")
        file.write(f"g_r: {g_r.tolist()} \n")
        file.write(f"gamma_c: {gamma_c.tolist()} \n")
        file.write(f"gamma_c_prime: {gamma_c_prime.tolist()} \n")
        file.write(f"delta_r: {delta_r.tolist()} \n")
        file.write(f"delta_r_prime: {delta_r_prime.tolist()} \n")
        file.write(f"epsilon: {epsilon} \n")
        file.write(f"sol_x: {sol_x} \n")
        file.write(f"sol_z: {sol_z} \n")

    # Delete the log file
    os.remove(log_file)
    os.remove("output/model.lp")
    os.remove("output/solutions.txt")

