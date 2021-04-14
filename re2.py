import re

#m=re.compile('\w+@\w+')
m=re.search('\w+@\w+', 'paulsun096@gmail.com')
print(m)

#bdays=re.compile('0-12+/+0-30+/+1996')
bdays=re.search('\d+/+\d+/\d\d\d\d', 'sfd4/2/1996sdf')
print(bdays)

#credit card number 
num='3245324323423451'
cc=re.search('\d{16}', num)
print(cc)
