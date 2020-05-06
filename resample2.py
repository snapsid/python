import re

x=open("resample2.txt")

a=""
for line in x:

    a=a+line
aa=re.findall('[0-9]+', a)

for i in range(0, len(aa)):
    aa[i] = int(aa[i])

count=0
for i in range(0, len(aa)):
    count=count+aa[i]
print(count)
