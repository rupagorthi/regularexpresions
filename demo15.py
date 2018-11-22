#valide name
import re
user_name=input("enter name:")
result=re.match("^[A-Za-z]*$",user_name)
if result==None:
    
    print("invalid name")
else:
    print("welcome Mr/Miss:",user_name)