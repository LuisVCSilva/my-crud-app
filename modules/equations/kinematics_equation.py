import z3
from flask import request, Blueprint
import pandas as pd
import json

kinematics_equation = Blueprint('kinematics_equation', __name__)

class Kinematics_equation:

   d, a, t, v_i, v_f = z3.Reals('d a t v__i v__f')
   equations = [d == v_i * t + (a*t**2)/2,v_f == v_i + a*t]
   parameters = {d:{'symbol':'d','description':'displacement of the object'},a:{'symbol':'a','description':'acceleration of the object'},t:{'symbol':'t','description':'time for which the object moved'},v_i:{'symbol':'v_i','description':'initial velocity of the object'},v_f:{'symbol':'v_f','description':'final velocity of the object'}}
   equations_latex = ["d = v_i t + \\frac{at^2}{2}","v_f = v_i + a t"]
   description = "These equations describes the mathematical relationship between the parameters of an object's motion. As such, they can be used to predict unknown information about an object's motion if other information is known"
   
   def __init__ (self):   
      self.functions = [show_kinematic_equations]
      self.text = ""

   def show_kinematic_equations(param): 
      if param==None:
         description = Kinematics_equation.description
         equations = pd.DataFrame(["$$" + x + "$$" for x in Kinematics_equation.equations_latex]).to_html(index=False,header=False)
         parameters = pd.DataFrame([["$$" + x["symbol"] + "$$", x["description"]] for x in list(Kinematics_equation.parameters.values())]).to_html(index=False,header=False)
         return {"Description":description,"Equations":equations,"Parameters":parameters}#(Kinematics_equation.equations_latex)
      else:
         problem = [Kinematics_equation.v_i == 0.0, Kinematics_equation.v_f == 4.10, Kinematics_equation.a   == 6.0]
         result = z3.solve(Kinematics_equation.equations + problem)
         print(result)
         return str(result)
         

   @kinematics_equation.route('/apps/kinematics_equation',methods=["GET"])
   def run():
      param = request.args["input"] if "input" in request.args else None
      result = Kinematics_equation.show_kinematic_equations(param)
      return json.dumps({"result":"$$"+result+"$$" if "input" in request.args else result})

   @kinematics_equation.route('/apps/critical_points/help',methods=["GET"])
   def help():
      return json.dumps({"text":"kinematics_equation help page"})    

   kinematics_equation_method = {'function_name':show_kinematic_equations,'keywords':['kinematic_equations','kinematic','kinematics']}
