#open a file and splits the string and extract float values and find average

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
a=0
c=0
for line in fh:
    line=line.strip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    a=a+float(line[20:])
    c=c+1   
print("Average spam confidence:", a/c)