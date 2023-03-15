###
#
# https://edabit.com/challenge/MhQbon8XzsG3wJHdP
#
# Solving Exponential Equations With Logarithms
# Create a function that takes a number a and finds the missing exponent x so that a when raised to the power of x is equal to b.
#
# Examples
# solve_for_exp(4, 1024) ➞ 5
#
# solve_for_exp(2, 1024) ➞ 10
#
# solve_for_exp(9, 3486784401) ➞ 10
# Notes
# a is raised to the power of what in order to equal b?
#
###

def solve_for_exp(a, b):
    exp_value = 1
    exp = 0
    while(exp_value <= b):
        if exp_value == b:
            return exp
        exp_value = exp_value * a
        exp+=1
    print("Not exponential!")
    return False


print(solve_for_exp(4, 1024) == 5)

print(solve_for_exp(2, 1024) == 10)

print(solve_for_exp(9, 3486784401) == 10)