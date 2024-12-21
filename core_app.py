#from flask_app import app
#import flaskcode
from flask import Blueprint, make_response, render_template, session, request, url_for
from time import sleep
import os
import uuid
from urllib.parse import quote
import json
from pathlib import Path
import time
from datetime import datetime
from werkzeug.routing import BuildError
import difflib




def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


MAX_COMPUTATION_TIME_PER_CLIENT = 30

core_app = Blueprint('core_app', __name__)

#core_app.config.from_object(flaskcode.default_config)
#core_app.config['FLASKCODE_RESOURCE_BASEPATH'] = 'userfiles'
#core_app.register_blueprint(flaskcode.blueprint, url_prefix='/flaskcode')


base = Path('sessions')

def getMetadata(t0):
 return {
 "duration":time.time()-t0,
 "computation_time_balance":MAX_COMPUTATION_TIME_PER_CLIENT-(time.time()-t0),
 "server_time":datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
 "user-agent":request.headers.get('User-Agent'),
 "ip":request.remote_addr
 }


def get_routes(app):
    routes = []
    for rule in app.url_map.iter_rules():
        route = {
            'endpoint': rule.endpoint,
            'methods': ','.join(sorted(rule.methods)),
            'path': str(rule),
        }
        routes.append(route)
    return routes

def doComputation(_input):
   sleep(1)
   output = {}

   # Get the base URL from an environment variable, default to localhost if not set
   base_url = os.getenv("BASE_URL", "http://localhost:5000")

   try:
      # Construct the target resource URL
      target_resource = f"{base_url}/{url_for(_input['text'].split()[0] + '.run')}"
      
      # Add query parameters if necessary
      if len(_input["text"].split()) > 1:
         target_resource += "?input=" + quote(" ".join(_input["text"].split()[1:]).encode("utf-8"))
      
      output = json.dumps({"url": target_resource})

   except BuildError as e:
      output = json.dumps({
         "error": "I couldn't understand... did you mean " +
         str(e).split("Did you mean ")[-1].split("'")[1].split(".")[0] +
         " instead of " + _input["text"].split()[0] + "?"
      })

   return output



@core_app.route('/evaluate/',methods=['GET','POST'])
def evaluate():
   t0 = time.time()
   if "call" in request.args:
      _meta = getMetadata(t0)
      _input = {"text":str(request.args["call"])}
      _output = doComputation(_input)
      dumpComputation(_meta,_input,_output)
      return _output
   return 0

def dumpComputation(_meta, _input, _output):
    session_id = session.get("id", "default_session")
    jsonpath = base / f"meta.json"  # Create the path for the session-specific meta.json file
    (base / session_id).mkdir(parents=True, exist_ok=True)
    with open(jsonpath, 'a' if os.path.exists(jsonpath) else 'w', encoding='utf-8') as file:
        file.write(json.dumps({'meta': _meta, 'input': _input, 'output': _output}, ensure_ascii=False, indent=4) + "\n")

@core_app.route('/login/',methods = ['GET','POST'])
def login():
   return make_response(render_template('login.html'))

@core_app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   resp.set_cookie('userID', user)
   return resp

@core_app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'

@core_app.route('/')
def main():
   resp = make_response(render_template('index.html'))
   if "id" not in session:
      resp.set_cookie('userID',str(uuid.uuid1()))
      os.makedirs('./sessions/',exist_ok=True)
      jsonpath = base / ("/meta.json")
      base.mkdir(exist_ok=True)
   return resp

def create_session():
   #session["id"] = str(uuid.uuid1())
   os.makedirs('./sessions/')

'''
if __name__ == '__main__':
    app.secret_key = "123"
    app.run(host='localhost', port=8080, debug=True)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    session.init_app(app)
    #db.create_all(app=app)
    #db.init_app(app)
    #db.create_all()
    #app.config.from_pyfile('settings.py')
    app.debug = True
'''
