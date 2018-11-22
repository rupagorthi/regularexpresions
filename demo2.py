# example program by using find all[re.search(pattern, string):

import re
st=input("enter string:")
result=re.search(r"rupa",st)
if "rupa"== "none":
    print(" match not found")
else:
    print("match found")
print(result)
print(result.group(0))