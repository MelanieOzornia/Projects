from fractions import Fraction

function = input("Do you want to differentiate or integrate?\nplease type 'd' for differentiate or 'i' for integrate\n")


co = input("what is the coefficient of x?\n")
ex = input("what is the exponent of x?\n")

# differentiation calculation
if function == "d":
    #prints result of derivative calculation
    print("The derivative of ", co, "x^", ex, " is: ", int(co) * int(ex), "x^", int(ex) - 1)
else:
    # integration calculation
    print("The integral of ", co, "x^", ex, " is: ", Fraction(int(co), int(ex) + 1), "x^", int(ex) + 1)