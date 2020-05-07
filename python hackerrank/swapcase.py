#swap case

#changing upper case to lower and vise versa


def swap_case(s):
    x=''
    for i in s:
        if i.isupper()==True:
            x=x+i.lower()
        elif i.islower()==True:
            x=x+i.upper()
        else:
            x=x+i
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)