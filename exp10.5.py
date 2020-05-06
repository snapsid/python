#open a file split its line extract day and than add the number of occurence to dictionary than printing in sort using list in tupples

fname = input("Enter file name: ")
fh = open(fname)

ls=list()
for a in fh:
    if a.startswith("From "):
        s=a.split()
        b=s[5]
        ls.append(b[0:2])
di=dict()   
for i in ls:
    di[i]=di.get(i,0)+1

ls1=list()
for k,v in di.items():
    ls1.append((k,v))

ls1=sorted(ls1)


for key,val in ls1:
    print(key, val)

