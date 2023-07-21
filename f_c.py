import numpy as np

def f_c(components, components_prime):
    """
    This functions tells us how similar two components are.
    Output:matrix of dimension len(components) x len(components_prime)

    For now: proportion of attributes that are equal
    """
    len_comp = len(components)
    len_comp_prime = len(components_prime)

    f_c_matrix = np.zeros((len_comp, len_comp_prime)).tolist() # initialize the matrix

    for c in range(len_comp):
        for c_prime in range(len_comp_prime):
            if components[c].type == components_prime[c_prime].type:
                total_number_attributes = max(len(components[c].attributes), len(components_prime[c_prime].attributes))
                if total_number_attributes == 0:
                    f_c_matrix[c][c_prime] = 1 #setze ich es null oder eins?
                else:
                    number_attributes_equal = 0
                    attributes = components[c].attributes
                    attributes_prime = components_prime[c_prime].attributes
                    for attribute in attributes:
                        for attribute_prime in attributes_prime:
                            if attribute.id == attribute_prime.id:
                                if attribute.param_value == attribute_prime.param_value:
                                    
                                    number_attributes_equal += 1
                    f_c_matrix[c][c_prime] = number_attributes_equal/total_number_attributes
            else:
                f_c_matrix[c][c_prime] = 0

    return f_c_matrix


