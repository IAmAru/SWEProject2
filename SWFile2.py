# Alejandro Jimenez Rocha / sai993

"""
SW Engineering Problem 2: 40 pts
Copy Software Files 2.1, 2.2, 2.3 into Pycharm. Using the files as templates,
create a class called Zfun that is capable of the following methods:
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy


class Zfun:
    """Constructor
    Stores a symbolic variable x
    Stores a symbolic function f(x)"""
    def __init__(self, fx, x):
        # I declared fx first so that the user doesn't have to declare x.
        self.x = x  # Stores x, as a symbolic value. With this, it's accessible by using Zfun().x
        self.fx = fx  # Stores f(x). By using the symbolic value x, we may modify it any way we want.
        # In this example, I decided to use (3x + 1). Multiplying 3*self.x (which is x), plus 1 we get our desired func.

    """Method 1: fa
    returns the function."""
    def fa(self, fx):
        return fx  # Simply returns the function we defined in the constructor.

    """Method 2: IntF:
    returns the symbolic integrate of f(x)."""
    def IntF(self, fx, x):
        """By using one of the sympy methods, integrate, we can throw in the function we desire to integrate and
        the variable which to integrate by. If, for example, the variable was self.y instead of self.x and we defined
        self.y as sympy.symbols('y'), it would do an integral in terms of y; and since there's no y in the function,
        the result would just be self.f * y, as everything else would be treated as a constant.
        """
        return sympy.integrate(fx, x)

    """Method 3: DifF:
    returns the symbolic derivative of f(x)"""
    def DifF(self, fx, x):
        """ # Similar to the above df. Only difference is it derives instead of integrating."""
        return sympy.diff(fx, x)

    """Method 4: PltF(a=start, b=end, deltF=stepsize)
    Plots(x[a,b,deltF], f(x), deltF)
    """
    def PltF(self, fx_coeff, fx_pow, fx_translation, x_axis=np.linspace(10, 20, 30)):
        # X takes in three values, both are defined below in v1 and v3.
        # fx takes in a function in terms of x. So, y = 3x + 1 would make it x*3 + 1, or since we're defining
        # our x here, 3 + 1 as default in case the user doesn't specify a function.
        # These are a, the starting point of the function, b, the ending point of the function, and stepsize, the
        # number of iterations the function goes through. For the sake of simplicity, I designated 10 as a, 20 as b,
        # and 30 as the step size as defaults, so it can be run without an arg saving us from potential errors.
        # This was done by using the linspace method of numpy and putting in the values desired.

        self.x_axis = x_axis  # Defines the x axis as what x is defined to. This makes sense... since it's x.
        self.y_axis = fx_coeff * x_axis ** fx_pow + fx_translation
        # Defines the y axis as the function of x. This makes sense as y = 3x + 1
        fig, ax = plt.subplots()
        ax.plot(self.x_axis, self.y_axis)  # This figures out the plot, using the parameters as reference.
        ax.set(xlabel='X Axis', ylabel='Y Axis', title='I hope this works!')
        ax.grid()
        fig.savefig("PleaseGiveMeAnA+.png")
        plt.show()


x_var = sympy.symbols('x')  # Defining x.
fx_c = 3  # Defining the coefficient, thing multiplying x. If it was ()x^2, this would be 1.
fx_p = 2  # Defining the power of x. If it was x() + 1, this would be 1.
fx_t = -7  # Defining how much to add to x. If this was 3x^2 (), this would be 0.

func_x = fx_c*x_var**fx_p+fx_t  # This makes sense. Coefficient times x, to the power of power, plus translation.

function = Zfun(func_x, x_var)  # Setting Zfun.
print(function.x)  # Accessing the x in Zfun, defined under the constructor as self.x.
print(function.fa(func_x))  # Accessing the fa() method.
print(function.DifF(func_x, x_var))  # Accessing the DifF() method.
print(function.IntF(func_x, x_var))  # Accessing the IntF() method.
v1 = np.linspace(10, 20, 30)
v3 = np.linspace(-10, 10, 29)
print(v3)
function.PltF(fx_c, fx_p, fx_t)  # Uses the PltF() method to plot the function provided under self.y_axis.
