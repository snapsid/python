hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate:")
r=float(rate)
s=0
if h>=40:
    s=s+(h-40)*r*1.5
    s=s+40*r
else:
    s=s+h*r
print(s)    
