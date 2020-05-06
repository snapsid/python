#open a file and print only email it uses startswith and splitfunctions

fname = input("Enter file name: ")
fh = open(fname)
count = 0
ls=list()
for a in fh:
    if a.startswith("From "):
        s=a.split()
        ls.append(s[1])
        count=count+1
for i in ls:
    print(i)


print("There were", count, "lines in the file with From as the first word")
