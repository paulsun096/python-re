import re

m=re.compile('\w+@\w+')
m=re.search("paulsun096@gmail.com", "paulsun096@gmail.com")

print(m)