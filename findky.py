# Branch: B1_FindKy
# A binary mixture of component A and B is in vapor-liquid equilibrium mixture
# inside a separation tank at temperature T and pressure P.
# This program is used to calculate the different molar compositions of both A & B
# in both liquid and gas phases
# please not that in the context of this problem, A & B are ib equilibrium
# Therefore: P_l = P_g & T_l = T_g

# Step 1: Define Variables:
# Component A = 1, Component B = 2
# l = liquid, g = gas
# x = Molar Composition % of Liquid
# y = Molar Composition % of Gas

# Given Equations:
# x1 + x2 = 1
# y1 + y2 = 1

# Equilibrium defined equations:
# k1 = y1 / x1 = num1
# k2 = y2 / x2 = num2
# In this problem, k1 = 1.5, and k2 = 0.3, but this program is designed
# to take any input variation of k1 and k2 and output the results based on that
# PROGRAM REQUIREMENTS: Problem MUST be in EQUILIBRIUM

# Solving for:
# Molar Composition: x1, x2, y1, y2
# Later, make the program capable of obtaining the
# above answer with any given pressure and temperature.


import numpy as np


# importing modules gives you access to all the function, objects and constructors that modules have to offer

# Part 1: Define equations and variables
# Givens:
# x1 + x2 = 1
# y1 + y2 = 1
# k1 = #1 = y1/x1
# k2 = #2 = y2/x2

# Rearrange to matrix format:
#  x1 + x2  +  0  +  0      = 1
#   0 +  0  + y1  + y2      = 1
# -#1 +  0  + y1  +  0      = 0
#   0 + -#2 +  0  + y2      = 0

# #x1   #x2     #y1     #y2      = #
#  1    1       0       0        = 1
#  0    0       1       1        = 1
# -#1   0       1       0        = 0
# -#2   0       0       1        = 0


# def degrees_of_freedom():
#     ask_eq = input("Write out the known and given equations. How many are there?: ")
#     eq_numb = float(ask_eq)
#     ask_var = input("Look at your equations and type in the number of unknowns to solve for: ")
#     unk_numb = float(ask_var)
#     print("You have ", eq_numb, " equations and ", ask_var, " unknowns")
#     dof = unk_numb - eq_numb
#     return dof


def main():
    ask_k1 = input("Please type in values for k1: ")
    k1 = float(ask_k1)
    ask_k2 = input("Please type in values for k2: ")
    k2 = float(ask_k2)
    x13 = -k1
    x24 = -k2
    print('k1 = ', k1, 'k2 = ', k2)
# a = np.array([[1, 0, x13, 0], [1, 0, 0, x24], [0, 1, 1, 0], [0, 1, 0, 1]])
# a = pd.DataFrame(np.random.rand(3),array([[1, 1, 0, 0], [0, 0, 1, 1], [x13, 0, 1, 0], [0, x24, 0, 1]]))
    a = np.array([[1, 1, 0, 0], [0, 0, 1, 1], [x13, 0, 1, 0], [0, x24, 0, 1]])
    b = np.array([1, 1, 0, 0])
    z = np.linalg.solve(a, b)
    z = np.round(z, 3)
    print('x1: ', z[0], ' x2: ', z[1], ' y1:', z[2], ' y2: ', z[3])

# print(a)
# print(b)
# Answer:
#  x1           x2        y1        y2
# [0.58333333 0.41666667 0.875      0.125     ]


main()
