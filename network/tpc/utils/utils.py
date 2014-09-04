__author__ = '1240'

import sympy as sy

class Util:

    def __init__(self):
        pass

    @staticmethod
    def eval_formula(formula, *kwargs):
        expr = sy.sympify(formula)
        return expr.evalf(subs=kwargs)
    #print(eval_formula(x=2, y=3, z=4, formula="sin(x*y*z)"))

    def get_heinz(self):


