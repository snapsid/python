#find the runner up score

n = int(input())
a= input()

ls=[]
ls=a.split()

for i in range(0, len(ls)): 
    ls[i] = int(ls[i])

ls = list(dict.fromkeys(ls))
ls.sort(reverse=True)
print(ls[1])

