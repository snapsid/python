#open a file find a line that using startswith and than spliting it and printing max number of email

fname = input("Enter file name: ")
fh = open(fname)

ls=list()
for a in fh:
    if a.startswith("From "):
        s=a.split()
        ls.append(s[1])
di=dict()   
for i in ls:
    di[i]=di.get(i,0)+1

k=0
v=0
for i,j in di.items():
    if i is None or j>k:
        v=i
        k=j
print(v,k)
