# example program by using find all[re.match(pattern, string):
import re
st=input("enter string:")
result=re.match(r"rupa",st)
if "rupa"== "none":
    print(" match not found")
else:
    print("match found")
print(result)
print(result.group())
print(result.start())
print(result.end())