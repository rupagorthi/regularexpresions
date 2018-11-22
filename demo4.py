#re.split(pattern, string)
import  re
st=input("enter string:")
result=re.split(r"r",st,)

print(result)

# re.split(pattern, string, [maxsplit=0]):
import  re
st=input("enter string:")
result=re.split(r"r",st,maxsplit=3)

print(result)