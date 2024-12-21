import json
from flask import Blueprint, request, session

get_session = Blueprint('get_session', __name__)

class Get_session:
   def __init__ (self):
      self.functions = [show_get_session]
      self.text = ""
      
   @staticmethod
   def show_get_session(func):
      return self.text 

   get_session_method = {'function_name':show_get_session,'keywords':['get_session']}
      
@get_session.route('/apps/get_session',methods=["GET"])
def run():
   return json.dumps({"text":session["id"]})   
