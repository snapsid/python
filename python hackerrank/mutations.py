#mututations 

def mutate_string(string, position, character):
    ls=list(string)
    ls[position]=character
    a=''.join(ls)
    return a

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)