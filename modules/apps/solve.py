import json
from flask import Blueprint,request
from sympy import latex,sympify
from sympy.abc import *

from sympy.solvers import solve as equation_solver

solve = Blueprint('solve', __name__)

class Solve:
   def __init__ (self):
      self.functions = [show_solve]
      self.text = ""
      
   @staticmethod
   def show_solve(eq):
      output = ""
      output = {"result":"$$" + latex(equation_solver(sympify(eq))) + "$$"}
      return output 

   @solve.route('/apps/solve/help',methods=["GET"])
   def help():
      return json.dumps({"text":"solve help page"}) 

   @solve.route('/apps/solve',methods=["GET"])
   def run():
      _input = request.args["input"]
      result = Solve.show_solve(sympify(_input))
      result = json.dumps(Solve.show_solve(request.args["input"]))
      return result
      
   solve_method = {'function_name':show_solve,'keywords':['solve']}
