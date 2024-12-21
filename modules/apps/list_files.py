import json, os, jsonify
from flask import Blueprint, request, session, jsonify

list_files = Blueprint('list_files', __name__)

class List_files:
   def __init__ (self):
      self.functions = [show_list_files]
      self.text = ""


   def list_files(directory):
      files_list = []
      for root, directories, files in os.walk(directory):
            for filename in files:
                  file_path = os.path.join(root, filename).split("/")[3:]
                  files_list.append(file_path)
      return files_list
      
   @staticmethod
   def show_list_files():
      files = List_files.list_files("./sessions/"+session["id"]+"/")
      return str((files))
      #return self.text 

   list_files_method = {'function_name':show_list_files,'keywords':['list_files']}
      
@list_files.route('/apps/list_files',methods=["GET"])
def run():
   return json.dumps({"text":List_files.show_list_files()})   
