#lists

#all the operation of list add remove etc

N = int(input())
ls=[]




def insert1(pos, num):
    ls.insert(pos, num)

def remove1(num):
    ls.remove(num)

def append1(num):
    ls.append(num)

def sort1():
    ls.sort()

def pop1():
    ls.pop()

def reverse1():
    ls.reverse()

def print1():
    print(ls)

while N>0:
    x=input()
    x=x.split()
    
    if x[0]=="insert":
        insert1(int(x[1]), int(x[2]))
    if x[0]=="print":
        print1()
    if x[0]=="remove":
        remove1(int(x[1]))
    if x[0]=="sort":
        sort1()
    if x[0]=="pop":
        pop1()
    if x[0]=="reverse":
        reverse1()
    if x[0]=="append":
        append1(int(x[1]))

    N=N-1