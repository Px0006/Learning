#Use matlotlib to implement a method

#plot (self, x1, x2, n_steps, filename)
#which plots the polynomial from point x1 to x2 in n_steps steps and saves the
#plot as a PDF in the filename file.

#You will need to create a list (or numpy array if you feel like trying a little
#more) with x values, an equal list of y values, and then call matplotlib's
#plot function.

#Also add a title to the figure that contains a string representation of the
#polynomial.

#Next, call savefig to save the plot to file.

#It is good to call clf () in matplotlib before each plot, otherwise you
#draw the polynomial on top of each other we repeated use.



import numpy as np
from matplotlib import pyplot as plt

def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print('# This is a polynomial of order {ord}')
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y

x = np.linspace(0, 9, 10)
coeffs = [1, 2, 3, 4, 5]
plt.plot(x, PolyCoefficients(x, coeffs))
plt.show()
