import json
from flask import Blueprint, request

credits = Blueprint('credits', __name__)

class Credits:
   def __init__ (self):
      self.functions = [show_credits]
      self.text = "<p>Dogemath is a easy to use mathematical engine</p><p>Made by Luis Vinicius Costa Silva</p><p>Meet me at Twitter/GitHub: @LuisVCSilva</p>"
   @staticmethod
   def show_credits(func):
      return self.text 

   @credits.route('/apps/credits',methods=["GET"])
   def run():
      return json.dumps({"text":["An app made by LuisVCSilva","<p>Dogemath is a easy to use mathematical engine</p><p>Made by Luis Vinicius Costa Silva</p><p>Meet me at Twitter/GitHub: @LuisVCSilva</p>"]})

   @credits.route('/apps/credits/help',methods=["GET"])
   def help():
      return json.dumps({"text":"credits help page"})   

   credits_method = {'function_name':show_credits,'keywords':['who','credits','who made this','what is this']}
