def variable_transfrmation(index:int, len_comp, len_comp_prime, len_rel, len_rel_prime):

    if index <= 0 or index > len_comp*len_comp_prime + len_rel*len_rel_prime:
        raise ValueError("invalid variable index")
    
   #check if x is variable for component or relation
    if index <= len_comp*len_comp_prime:
        #index is variable for component
        matrix = "components"
        row = (index-1) // len_comp +1
        column = (index-1) % len_comp_prime +1
        return row, column, matrix
    else:
        # Index is variable for relation
        matrix = "relations"
        row = ((index - len_comp*len_comp_prime)-1) // len_rel +1
        column = ((index - len_comp*len_comp_prime) -1) % len_rel_prime +1
        return row, column, matrix
    
if __name__== "__main__":
    index = 59
    len_comp = 44
    len_comp_prime = 44
    len_rel = 42
    len_rel_prime = 42
    row, column, matrix = variable_transfrmation(index, len_comp, len_comp_prime, len_rel, len_rel_prime)
    print(f"The variable is in the {matrix}-matrix in row {row}, column {column}")