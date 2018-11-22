# Return the first two character of each word
#Solution-1 Extract consecutive two characters of each word, excluding spaces (using “\w“)
import re
s1 = "rupa learning python and django"
result = re.findall(r"\w\w",s1)
print(result)
print("===============================")

#Extract consecutive two characters those available at start of word boundary (using “\b“)
import re
s1 = "rupa learning python and django"
result = re.findall(r"\b\w",s1)
print(result)

print("===============================")
import re
s1 = "rupa learning python and django"
result = re.findall(r"\w.",s1)
print(result)

print("===============================")
import re
s1 = "rupa learning python and django"
result = re.findall(r"\w\w.",s1)
print(result)