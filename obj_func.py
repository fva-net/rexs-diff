import numpy as np

def obj_func(components, components_prime, relations, relations_prime, f_c, g_r, gamma_c, gamma_c_prime, delta_r, delta_r_prime, epsilon):
    len_comp = len(components)
    len_comp_prime = len(components_prime)
    len_rel = len(relations)
    len_rel_prime = len(relations_prime)

    # Define the variables
    x_rows = len_comp
    x_cols = len_comp_prime
    z_rows = len_rel
    z_cols = len_rel_prime

    # Define the variables
    x = np.identity(x_rows).tolist()
    z = np.identity(z_rows).tolist()

    #objective function
    T1 = sum(f_c[i][j] * x[i][j] for i in range(x_rows) for j in range(x_cols)) # Reward term 1 for the components
    T2 = sum(g_r[k][l] * z[k][l] for k in range(z_rows) for l in range(z_cols)) # Reward term 2 for the relations
    T3 = sum(gamma_c[i] * (1 - sum(x[i][j] for j in range(x_cols))) for i in range(x_rows)) # Penalty term for unmatched components in the first data model
    T4 = sum(gamma_c_prime[j] * (1- sum(x[i][j] for i in range(x_rows))) for j in range(x_cols)) # Penalty term for unmatched components in the second data model
    T5 = sum(delta_r[k] * (1 - sum(z[k][l] for l in range(z_cols))) for k in range(z_rows)) # Penalty terms for unmatched relations in the first data model
    T6 = sum(delta_r_prime[l] * (1 - sum(z[k][l] for k in range(z_rows))) for l in range(z_cols)) # Penalty term for unmatched relations in the second data model
    T7 = 0
    for c in range(x_rows):
        for c_prime in range(x_cols):
            if components[c].type != components_prime[c_prime].type:
                T7 += epsilon *x[c][c_prime]

    objective = T1+T2-T3-T4-T5-T6-T7

    return objective

