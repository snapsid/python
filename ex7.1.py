#code for opening a text file and printing in upper case

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for a in fh:
    a=a.strip()
    print(a.upper())
