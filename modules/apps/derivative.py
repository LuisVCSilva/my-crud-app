import json
from flask import Blueprint, request
from .utils.derivative_steps import *
from sympy import latex, Derivative as compute_derivative
from sympy.abc import *

derivative = Blueprint('derivative', __name__)

class Derivative:
   def __init__ (self):
      self.functions = [show_derivative]
      self.text = ""
      
   @staticmethod
   def show_derivative(eq,show_steps):
      return print_html_steps(eq,x) if show_steps==True else latex(compute_derivative(eq).doit())

   @derivative.route('/apps/derivative',methods=["GET"])
   def run():
      return json.dumps({"result":"$$"+Derivative.show_derivative(request.args["input"].replace("steps",""),"steps" in request.args["input"])+"$$"})

   @derivative.route('/apps/derivative/help',methods=["GET"])
   def help():
      return json.dumps({"text":"derivative help page"})     
      
   derivative_method = {'function_name':show_derivative,'keywords':['derivative']}
