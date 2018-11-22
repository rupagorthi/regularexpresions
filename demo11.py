#return the domain type of given email-id's
import re
st="sadiqraj@gmail.comraja@yahoo.comsadiqraj8282@co.in"
result=re.findall(r"@\w+",st)
print(result)
