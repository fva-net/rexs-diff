import numpy as np

def f_c(components: list , components_prime: list):
    """
    This functions tells us how similar two components are.
    Output: matrix of dimension len(components) x len(components_prime)

    For now: proportion of attributes that are equal
    """
    len_comp = len(components)
    len_comp_prime = len(components_prime)

    f_c_matrix = np.zeros((len_comp, len_comp_prime)) # initialize the matrix

    for c in range(len_comp):
        for c_prime in range(len_comp_prime):
            if (components[c].type == "concept_bearing" and components_prime[c_prime].type in ["concept_bearing", "rolling_bearing_with_catalog_geometry", "rolling_bearing_with_detailed_geometry", "slide_bearing"]) or (components[c].type == "rolling_bearing_with_catalog_geometry" and components_prime[c_prime].type in ["concept_bearing", "rolling_bearing_with_catalog_geometry", "rolling_bearing_with_detailed_geometry", "slide_bearing"]) or (components[c].type == "rolling_bearing_with_detailed_geometry" and components_prime[c_prime].type in ["concept_bearing", "rolling_bearing_with_catalog_geometry", "rolling_bearing_with_detailed_geometry"]) or (components[c].type == "slide_bearing" and components_prime[c_prime].type in ["concept_bearing", "slide_bearing"]) or (components[c].type in ["coupling", "switchable_coupling" ] and components_prime[c_prime].type in ["coupling", "switchable_coupling"]) or (components[c].type == components_prime[c_prime].type):
                total_number_attributes = max(len(components[c].attributes), len(components_prime[c_prime].attributes))
                if len(components[c].attributes) == 0 and len(components_prime[c_prime].attributes) == 0:
                    f_c_matrix[c][c_prime] = 1
                # TODO: empty list of attributes
                elif min(len(components[c].attributes), len(components_prime[c_prime].attributes)) == 0:
                    f_c_matrix[c][c_prime] = 0.1
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


if __name__ == "__main__":
    matrix = np.array([[1,2,3],[4,5,6]])
    print(matrix[0][1])