import json
from flask import Blueprint, request

from sympy import latex, Derivative, solve
from sympy.abc import *

critical_points = Blueprint('critical_points', __name__)

class Critical_points:
   def __init__ (self):
      self.functions = [show_critical_points]
      self.text = ""
      
   @staticmethod
   def show_critical_points(eq):
      resp = ""
      output = solve(Derivative(eq).doit())
      resp = "\left\{\\begin{matrix}" + "\\\\".join([(latex(x)) for x in output])  + "\end{matrix}\\right."
      return resp

   @critical_points.route('/apps/critical_points',methods=["GET"])
   def run():
      return json.dumps({"result":"$$"+Critical_points.show_critical_points(request.args["input"])+"$$"})

   @critical_points.route('/apps/critical_points/help',methods=["GET"])
   def help():
      return json.dumps({"text":"critical_points help page"})    

   critical_points_method = {'function_name':show_critical_points,'keywords':['critical_points']}
