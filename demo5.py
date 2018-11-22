# example program by using find all[re.sub(pattern, repl, string):
import re
st = "Current rocking programming is .net"
result = re.sub(r".net","Python",st)
print(result)

print("==================================")
import re
st= input("enter string:")
result = re.sub(r"java","Python",st)
print(result)
