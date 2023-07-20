from pyscipopt import Model
model = Model()

# Variablen einführen
rows = 2
cols = 2
x = [[model.addVar()for i in range(cols)]for j in range(rows)]

# set objective function
model.setObjective(x[0][0]+3*x[1][1], sense = 'maximize')

# add constraints
model.addCons(x[0][0]+x[1][1] <= 3)
model.addCons(2*x[0][0]+4*x[1][1]<=20)

# solve the problem
model.optimize()

# get the best solution
sol = model.getBestSol()

z = model.getObjVal()
x_opt = model.getVal(x[0][0])
y_opt = model.getVal(x[1][1])
w_opt = model.getVal(x[0][1])
v_opt = model.getVal(x[1][0])	

print("Best solution is:")
print(sol)
print("The objective value is:")
print(z)
print("The value of the variable x is:")
print(x_opt)
print("The value of the variable y is:")
print(y_opt)
print("The value of the variable w is:")
print(w_opt)
print("The value of the variable v is:")
print(v_opt)