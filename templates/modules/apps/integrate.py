import json
from flask import Blueprint, request
#from .utils.integral_steps import *
from sympy import latex, integrate as compute_integral
from sympy.abc import *

integrate = Blueprint('integrate', __name__)

class Integrate:
   def __init__ (self):
      self.functions = [show_integrate]
      self.text = ""
      
   @staticmethod
   def show_integrate(eq,show_steps):
      return latex(compute_integral(eq))#print_html_steps(eq,x) if show_steps==True else latex(compute_integral(eq))       

   @integrate.route('/apps/integrate',methods=["GET"])
   def run():
      return json.dumps({"result":"$$"+Integrate.show_integrate(request.args["input"].replace("steps",""),"steps" in request.args["input"]) + "$$"})

   @integrate.route('/apps/integrate/help',methods=["GET"])
   def help():
      return json.dumps({"text":"integrate help page"})   

   integrate_method = {'function_name':show_integrate,'keywords':['integrate']}
