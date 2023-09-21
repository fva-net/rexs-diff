import numpy as np

def f_c(components: list, components_prime: list):
    """
    This functions tells us how similar two components of the two models are. It calculates the proportion of attributes that are equal.\n
    Input:
        - components: list of components of the model A\n
        - components_prime: list of components of the model B\n
    Output: 
        - matrix of dimension len(components) x len(components_prime)
    """
    len_comp = len(components)
    len_comp_prime = len(components_prime)

    f_c_matrix = np.zeros((len_comp, len_comp_prime)) # initialize the matrix

    # go through every component of model A and every component of model B and calculate the proportion of equal attributes
    for c in range(len_comp):
        for c_prime in range(len_comp_prime):
            # check if the components are of the same type and if they are, calculate the proportion of equal attributes. There are exceptions for the bearing types and the coupling types. They may be matched with each other. 
            if (components[c].type == "concept_bearing" and components_prime[c_prime].type in ["concept_bearing", "rolling_bearing_with_catalog_geometry", "rolling_bearing_with_detailed_geometry", "slide_bearing"]) or (components[c].type == "rolling_bearing_with_catalog_geometry" and components_prime[c_prime].type in ["concept_bearing", "rolling_bearing_with_catalog_geometry", "rolling_bearing_with_detailed_geometry", "slide_bearing"]) or (components[c].type == "rolling_bearing_with_detailed_geometry" and components_prime[c_prime].type in ["concept_bearing", "rolling_bearing_with_catalog_geometry", "rolling_bearing_with_detailed_geometry"]) or (components[c].type == "slide_bearing" and components_prime[c_prime].type in ["concept_bearing", "slide_bearing"]) or (components[c].type in ["coupling", "switchable_coupling" ] and components_prime[c_prime].type in ["coupling", "switchable_coupling"]) or (components[c].type == components_prime[c_prime].type):
                total_number_attributes = max(len(components[c].attributes), len(components_prime[c_prime].attributes)) # calculate the max number of attributes 
                # special case: both components have zero attributes
                if len(components[c].attributes) == 0 and len(components_prime[c_prime].attributes) == 0:
                    f_c_matrix[c][c_prime] = 1
                # special case: one component has zero attributes
                elif min(len(components[c].attributes), len(components_prime[c_prime].attributes)) == 0:
                    f_c_matrix[c][c_prime] = 0.1
                # general case: calculate the proportion of equal attributes
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
            # if the components are not of the same type, set the value of the matrix to -10
            else:
                f_c_matrix[c][c_prime] = -10
    return f_c_matrix
