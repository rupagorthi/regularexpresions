# example program by using find all[re.findall (pattern, string):
import re
st=input("enter string:")
result=re.findall(r"rupa",st)
if "rupa"== "none":
    print(" match not found")
else:
    print("match found")
print(result)