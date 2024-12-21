#DO NOT EDIT THIS FILE
import json
from flask import Blueprint, request
from sympy import Matrix, sympify, latex

eigenvalue = Blueprint('eigenvalue', __name__)

class Eigenvalue:
   def __init__ (self):
      self.functions = [show_eigenvalue]
      self.text = ""
      
   @staticmethod
   def show_eigenvalue(expression):
      expression = sympify(expression)
      expression = Matrix(expression)
      output = latex(expression.eigenvals())
      return output

   @eigenvalue.route('/apps/eigenvalue',methods=["GET"])
   def run():
      expression = request.args["input"]
      return json.dumps({"text":"$$" + Eigenvalue.show_eigenvalue(expression) + "$$"})   

   @eigenvalue.route('/apps/eigenvalue/help',methods=["GET"])
   def help():
      return json.dumps({"text":"eigenvalue help page"}) 

   eigenvalue_method = {'function_name':show_eigenvalue,'keywords':['eigenvalue']}