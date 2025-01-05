num1=float(input("enter a value of num1 "))
num2=float(input("enter a value of num2 "))
while (True):
    operator=input("choose operator")
    if operator=="+":
      print(f"additon:{num1+num2}")
    elif operator=="-":
      print("Subraction:",num1-num2)
    elif operator=="/":
      if num2==0:
        print("num2 is not divisible by 0")
      else:
        print("Division:",num1/num2)
    elif operator=="*":
      print(f"Multliplication:{num1*num2}")
    elif operator=="%":
      print(f"Modular division:{num1%num2}")
    else:
      print("Invalid operator please enter the following (+,-,*,/,%) operators ")
     