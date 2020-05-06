#try except and print largest and smallest

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        n=int(num)
        if largest==None:
            largest=n
            smallest=n
        else:
            if n>largest:
                largest=n
            if n<smallest:
                smallest=n
    except:
        print("Invalid input")
            
    

print("Maximum is", largest)
print("Minimum is", smallest)