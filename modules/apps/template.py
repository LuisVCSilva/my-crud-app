import json
from flask import Blueprint, request

template = Blueprint('template', __name__)

class Template:
   def __init__ (self):
      self.functions = [show_template]
      self.text = ""
      
   @staticmethod
   def show_template(func):
      return self.text 

   @template.route('/apps/template',methods=["GET"])
   def run():
      return json.dumps({"text":"template page"})

   @template.route('/apps/template/help',methods=["GET"])
   def help():
      return json.dumps({"text":"template help page"})       

   template_method = {'function_name':show_template,'keywords':['template']}
