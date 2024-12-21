import json
from flask import Blueprint, request, url_for, jsonify
import requests
import os

help = Blueprint('help', __name__)

class Help:
    def __init__(self):
        self.functions = [self.show_help]
        self.text = ""
    
    @staticmethod
    def show_help():
        # Get a list of Python files (modules) in the current directory
        modules = [
            "about.py", "clear.py", "credits.py", "critical_points.py", "derivative.py", 
            "eigenvalue.py", "eigenvector.py", "get_session.py", "help.py", "integrate.py", 
            "is_odd.py", "list_files.py", "login.py", "logout.py", "show.py", "signup.py", 
            "simplify.py", "solve.py", "taylor_series.py", "template.py"
        ]

        # Generate help statements for each module
        help_statements = []
        for module in modules:
            module_name = module.replace(".py", "")
            help_statement = f"{module_name}<br>"
            help_statements.append(help_statement)
        
        # Return the help statements as a string
        return "\n".join(help_statements)

    help_method = {'function_name': show_help, 'keywords': ['help']}
      
@help.route('/apps/help', methods=["GET"])
def run():
    return json.dumps({"text": Help.show_help()})

