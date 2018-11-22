#return all worlds of a string those starts wiht vowel
import re
st="i am learning python wiht naveen sir"
result=re.findall(r"\w+",st)
print(result)

print("****************************")
import re
st="iam learing python with naveen sir "
result=re.findall(r"[aeiouAEIOU]\w+",st)
print(result)