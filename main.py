from art import logo
import os
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def multi(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":sub,
  "*":multi,
  "/":divide,
}

def calculator():
  print(logo)

  number_one= float(input("Enter the first number"))
  for keys in operations:
    print(keys)

  if_yes = False
  while not if_yes:
    pick_operation= input("Pick an operation")
    
    number_two= float(input("What is the next number"))
  
    calculation_function = operations[pick_operation]
    answer = calculation_function(number_one,number_two)
    
    print(f"{number_one} {pick_operation} {number_two} = {answer}")
    
    option= input(f"Press 'y' to continue with {answer}, or type 'n' to start a new calculation")  
  
    if option == "y":
      #if_yes=False
      number_one=answer
    else:
      if_yes=False
      os.system("cls")
      calculator()

calculator()      
    


