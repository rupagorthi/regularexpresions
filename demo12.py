#exact only domine name using"()":
import re
st="rupanaidu81@gmail.com rupanaidu81@yahoo.com rupanaidu81python@co.in"
result=re.findall(r"@\w+.\w+",st)
print(result)