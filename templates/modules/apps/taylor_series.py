import json
from flask import Blueprint, request

taylor_series = Blueprint('taylor_series', __name__)

class Taylor_series:
   def __init__ (self):
      self.functions = [show_taylor_series]
      self.text = ""
      
   @staticmethod
   def show_taylor_series(func):
      return self.text 

   @taylor_series.route('/apps/taylor_series',methods=["GET"])
   def run():
      return json.dumps({"text":"taylor_series page"})  

   @taylor_series.route('/apps/taylor_series/help',methods=["GET"])
   def help():
      return json.dumps({"text":"taylor series help page"})       


   taylor_series_method = {'function_name':show_taylor_series,'keywords':['taylor_series']} 
