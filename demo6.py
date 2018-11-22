import re
s1 = "rupa  learning python and django"
result = re.findall(r".\w",s1)
print(result)

print('==============================')
import re
s1 = "rupa learning python and django"
result = re.findall(r".",s1)
print(result)

#Above, space is also extracted, now to avoid it use “\w” instead of “.“.

import re
s1 = "rupa learning python and django"
result = re.findall(r"\w",s1)
print(result)





