from math import *
l=float(input("enter the length of classroom in feet:"));
b=float(input("enter the breath of classroom in  feet:"));
h=float(input("enter the height of classroom in  feet:"));
vol=l*b*h
print("volume of the room is:",vol)
#converting
x=vol/1500
#p=x*1.5
s=vol/2000
p=vol/1000
y=ceil(x)
q=ceil(p)
t=ceil(s)

print("you will need ",y,"1.5T A/c")
print("you will need ",p,"1T A/c")
print("you will need ",t,"2T A/c")