import sys

def main(args):
   with open('template.txt', 'r') as f:
       new_module_name = args[0]
       src = f.read()
       result = src.replace("template",new_module_name).replace("Template",new_module_name.capitalize())
       f = open("modules/"+new_module_name+".py", "w")
       f.write(result)
       f.close()
       
if __name__=='__main__':
    main(sys.argv[1:]) 
