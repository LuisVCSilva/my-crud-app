import json
from flask import Blueprint, request

about = Blueprint('about', __name__)

class About:
   def __init__ (self):
      self.functions = [show_about]
      self.text = "<p>Web-based terminal written in Flask</p><p>Made by Luis Vinicius Costa Silva</p><p>Meet me at Twitter/GitHub: @LuisVCSilva or luisvcsilva.netlify.app</p>"
   @staticmethod
   def show_about(func):
      return self.text 
   
   @about.route('/apps/about',methods=["GET"])
   def run():
      return json.dumps({"text":"An app made by LuisVCSilva"})

   @about.route('/apps/about/help',methods=["GET"])
   def help():
      return json.dumps({"text":"about help page"})   
      
   about_method = {'function_name':show_about,'keywords':['who','about','who made this','what is this']}
