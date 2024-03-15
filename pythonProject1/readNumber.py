import re
hand = open ('C:\\Users\\renug\\OneDrive\\Documents\\regex_sum_1952712.txt')
x=list()
for line in hand:
    y=re.findall('[0-9]+',line)
    x=x+y
sume=0
for i in x:
    sume=sume+ int(i)
print (sume)