# Alejandro Jimenez Rocha / sai993

"""Problem 3: 50 pts
Review the well-known Newton's method for finding the roots of a function f(x) = 0.
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy
from SWFile2 import Zfun  # Importing Zfun from SWFile2.

"""
Step A: Create a child class called NewtMeth that inherits from a parent class Zfun
NewtMeth that computes the values of x that result in f(x) = 0.
"""


class NewtMeth(Zfun):
    def __init__(self, fx, x):
        self.fx = fx
        self.x = x
        super().__init__(fx, x)
        self.f_prime = Zfun(fx, x).DifF(fx, x)  # Calling on DifF to grant me the derivative of my equation.

    def ZNewtCalc(self):
        """Method 1: ZNewtCalc(f, f', x_0, e, N)
               f > f(x)
               f' > f'(x) = d(f(x)/dx)
               x_o: initial guess
               e: stepsize
               N: number of Newton-method iterations

               Returns the values of x for which f(x) = 0."""
        if self.f_prime == 0:  # Just a precaution to not always be getting 0.
            "This function has no continuous derivative."
        else:
            for n in range(iterations-1):
                x_n = (x_naught - epsilon*n)
                x_n_plus_1 = x_n - ((fx_coeff * x_n ** fx_pow - fx_translation) / ((self.f_prime / self.x) * x_n))
                if x_n_plus_1 == 0:
                    self.x_n = x_n
                    return self.x_n
                else:
                    pass
                if n == iterations:
                    print(f"Procedure completed unsuccessfully after {iterations} iterations.")
                else:
                    pass

    def PltNewtCalc(self):
        """Method 2: PltNCalc(f, x_o, e, N)
        Plot out the function and its roots
        a. Plots the functions f(x) using the matplotlib package.
        b. On the same plat print the values of x for which f(x) = 0"""
        zeroNumberOne = int(self.x_n)  # Ridding myself of self.x_n.
        zeroNumberTwo = -zeroNumberOne  # The rule of two applies here.
        x_axis = np.linspace(zeroNumberOne, zeroNumberTwo, 30)
        y_axis = fx_coeff * x_axis ** fx_pow + fx_translation
        fig, ax = plt.subplots()
        ax.plot(x_axis, y_axis)
        ax.set(xlabel='X Axis', ylabel='Y Axis', title=f'The solutions for {func_x}=0 are {zeroNumberOne} and '
                                                       f'{zeroNumberTwo}.')
        ax.grid()
        fig.savefig("PrettyPlease.png")
        plt.show()
        print(f"The solutions for {func_x}=0 are {zeroNumberOne} and {zeroNumberTwo}.")


x_var = sympy.symbols('x')  # Defining x.
fx_coeff = 1  # Defining the coefficient, thing multiplying x. If it was ()x^2, this would be 1.
fx_pow = 2  # Defining the power of x. If it was x() + 1, this would be 1.
fx_translation = -4  # Defining how much to add to x. If this was 3x^2 (), this would be 0.
func_x = fx_coeff*x_var**fx_pow+fx_translation

"""Because using 3x^2 -7 would be very difficult given its solution would be sqrt(7/3), I'm going to opt to use a more
precise equation, x^2-4, where the answer would just be 2."""

x_naught = 3  # Just a guess at what we believe the solution might be close to.
epsilon = 0.25  # Also just a guess, but this time the step size we wish to iterate through to reach the solution.
iterations = 100  # Yet another guess! But this is how many times we believe it'd take to get to the solution.

newtMeth = NewtMeth(func_x, x_var)  # Setting NewtMeth.
newtMeth.ZNewtCalc()  # Accessing the ZNewtCalc method.
newtMeth.PltNewtCalc()  # Accessing the PltNewtCalc method.
