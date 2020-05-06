def computepay(h,r):
    s=0
    if h>=40:
        s=s+(h-40)*r*1.5
        s=s+40*r
    else:
    	s=s+h*r
    return s

hrs = float(input("Enter Hours:"))
rate=float(input("Enter Rate:"))


p = computepay(hrs,rate)

print("Pay",p)