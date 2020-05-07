#string split and join

#using split() function and join()

#join list to string and adding "-" between them

def split_and_join(line):
    line=line.split()
    line="-".join(line)
    return line
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)