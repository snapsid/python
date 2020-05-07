#find a string

#checking how many times substring occurs in the string 

#using startswith() inside for loop 

def count_substring(string, sub_string):

    count1=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count1=count1+1
    return count1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)