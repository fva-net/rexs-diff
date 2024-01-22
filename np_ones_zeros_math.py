
def ones(countx: int, county:int): 
    return [[1. for _ in range(county)] for _ in range(countx)]

def zeros(countx: int, county:int): 
    return [[0. for _ in range(county)] for _ in range(countx)]

def check_tolerance(a, b, abs_tol=0.0, rel_tol=1e-09, check_both=False):
    if type(abs_tol) is float and type(rel_tol) is float: 
        if check_both:
            return abs(a-b) <= min(rel_tol * max(abs(a), abs(b)), abs_tol) 
        else:
            return (abs(a-b) <= rel_tol * max(abs(a), abs(b))) or (abs(a-b) <= abs_tol)
    else: 
        raise Exception("The values of abs or tol are wrong "+ str(abs_tol)+" "+str(rel_tol) +" "+ str(a)+ " "+ str(b))

def check_equality(a, b, abs=0.0, rel=1e-09, check_both=False):
    if type(a) is float and type(b) is float:
        return check_tolerance(a, b, abs, rel,check_both)
    if type(a) is list and type(b) is list:
        isEqual = True
        for a0, b0 in zip(a,b):
           isEqual &= check_equality(a0, b0, abs, rel,check_both) 
        return isEqual
    return a == b

# print(check_equality(0.2,   0.4,    0.1,    0.1,check_both=False)) #should be false
# print(check_equality(0.2,   0.3,    0.1,    0.2,check_both=False)) #should be true
# print(check_equality(0.2,   0.3,    0.51,   0.1,check_both=False)) #should be true
# print(check_equality(0.2,   0.3,    0.2,    0.11,check_both=True)) #should be false
# print(check_equality(0.2,   0.3,    0.50,   0.4,check_both=True)) #should be true
# print(check_equality(2.0,   3.0,    0.01,   2.0,check_both=True)) #should be false
# print(check_equality(2.0,   3.0,    0.01,   2.0,check_both=False)) #should be true

# print(check_equality([0.2,2.0],[0.4,3.0],0.1,2.0,False))  #should be true
# print(check_equality([0.2,2.0],[0.4,3.0],0.1,2.0,True)) #should be false