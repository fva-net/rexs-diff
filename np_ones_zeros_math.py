
def ones(countx: int, county:int): 
    return [[1. for _ in range(county)] for _ in range(countx)]

def zeros(countx: int, county:int): 
    return [[0. for _ in range(county)] for _ in range(countx)]

def check_tolerance(a, b, rel_tol=1e-09, abs_tol=0.0, check_both=False):
    if check_both:
        return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol) 
    else:
        return abs(a-b) <= min(rel_tol * max(abs(a), abs(b)), abs_tol) 
        

def check_equality(a, b, abs=0.0, rel=1e-09, check_both=False):
    if type(a) is float and type(b) is float:
        return check_tolerance(a, b, rel, abs)
    if type(a) is list and type(b) is list:
        isEqual = True
        for a0, b0 in zip(a,b):
           isEqual &= check_equality(a0, b0, abs, rel) 
        return isEqual
    return a == b