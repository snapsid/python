#nested list

#concept of nested list, smallest value in list, 2nd smallest value, sorting of list

ls=[]
num=int(input())
for _ in range(num):
    name = input()
    score = float(input())
    ls.append([score, name])

ls.sort()

#list sorted therefore val = smallest value
val=ls[0][0]

ls1=[]

#val2=max value from the list
val2=ls[num-1][0]

#finding 2nd largest value and storing it to val2
for i in range(num):
    if ls[i][0]<val2 and ls[i][0]>val:
        val2=ls[i][0]    


#adding all the name of 2nd last to ls1 list
for i in range(num):
    if(ls[i][0])==val2:
        ls1.append(ls[i][1])

ls1.sort()
#ls1 sorted to print in ascending order

for i in ls1:
    print(i)

