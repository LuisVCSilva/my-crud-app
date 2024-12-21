import json
from flask import Blueprint, request,url_for, jsonify
import requests

help = Blueprint('help', __name__)

class Help:
   def __init__ (self):
      self.functions = [show_help]
      self.text = ""
      
   @staticmethod
   def show_help():
       list_apps_url = url_for('list_apps', _external=True)
       response = [(item["path"].split("/")[-1],url_for(item["path"].split("/")[-1]+".run")) for item in requests.get(list_apps_url).json() if (item["path"].split("/")[-1])!="help"]
       print(response)
       return str(response)

   help_method = {'function_name':show_help,'keywords':['help']}
      
@help.route('/apps/help',methods=["GET"])
def run():
   return json.dumps({"text":Help.show_help()})   
