# Extract each word (using “*” or “+“)

import re
s1 = "rupa learning python and django"
result = re.findall(r"\w*",s1)
print(result)

# Now to remove spaces we will go  with+

import re
s1 = "rupa learning python and django"
result = re.findall(r"\w+",s1)
print(result)
