import re
input=input("enter a input string:")
m=re.match("\d{5}\Z",input)
if m:
    print("True")
else:
    print("False")