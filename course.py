# EXECUTING A PROLOG PROGRAM AND GETTING BACK RESUTLS

import os

# Calculating the length of a given list using Prolog

def initialization(rule:str, args:list)->str:
  # This function accepts a rule name, and
  # the list of its arguments and 
  # return the Prolog's initialization
  # rule for the execution
  template = ":- initialization "
  template += rule + "(" + args + ","
  
  R = "R" # where the result will be stored (can be multiple, so changed to your needs)
  template += R
  template += ")"
  
  # Writing the result (the variable with the indx_result)
  template += ", writeln(" + R + ")"
  
  # Halting
  template += ", halt."
  print("Template is: ", template)
  return template

def execute_prolog(file_name:str, output_fl:str):
  # execute the content of the prolog file and
  # saves the output to a output_fl file
  print("Command is " + "swipl -s " + file_name + " > " + output_fl)
  os.system("swipl -s " + file_name + " > " + output_fl)

def read_file(file:str)->str:
  # Return the content of the file
  f = open(file, "r")
  out = f.readline()
  f.close()
  return out

def append_2_file(file:str, content:str)->str:
  # Write the content to the file
  # Return the original content
  f = open(file, "r")
  original = f.read()
  f.close()
  f = open(file, "a")
  f.write("\n")
  f.write(content)
  return original

def write_2_file(file:str, content:str)->None:
  # Delete the previous content and write down 
  # the new one
  f = open(file, "w")
  f.write(content)

def read_args()->list:
  args = "["
  print("Enter the list elements [# when finished]:")
  a = input("elt: ")
  while a != '#':
    if a != '':
      args += a + ","
    a = input("elt: ") 
  args = args[:-1]
  args += "]"
  return args


prolog_file_name = "test.pl"
rule = "len" # The rule/clause to call
args = read_args() # read list elements from the user
result_fl = "result.txt" # the file where to save the output of the Prolog's program

original = append_2_file(prolog_file_name, initialization(rule, args)) 
execute_prolog(prolog_file_name, result_fl)
output = read_file(result_fl)
print("The output is ", output)
# Reset the original conent of the .pl file
write_2_file(prolog_file_name, original)