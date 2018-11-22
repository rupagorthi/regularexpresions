# to search if an e-mail address is in a string:
import re
input="contact me by sadiqraj8282@gmail.com or at the office. "
m=re.search("[^@]+@[^@]+\.[^@]+",input)
if m:
    print("string found.")
else:
    print("nothing found")