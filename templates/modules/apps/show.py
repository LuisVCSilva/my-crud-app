import json
from flask import Blueprint, request, session

show = Blueprint('show', __name__)

class Show:
   def __init__ (self):
      self.functions = [show_show]
      self.text = ""
      
   @staticmethod
   def show_show(file_path):
      saida = ""
      with open(file_path, 'r') as file:
            for line in file:
                  saida = saida + line.strip()
      return saida 

   show_method = {'function_name':show_show,'keywords':['show']}
      
@show.route('/apps/show',methods=["GET"])
def run():
   return json.dumps({"text":Show.show_show("./sessions/"+session["id"]+"/"+request.args["input"])})   
