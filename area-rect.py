l=float(input("enter the length of classroom in meters:"));
b=float(input("enter the breath of classroom in  meters:"));
h=float(input("enter the height of classroom in  meters:"));
area=2*(h*b)+2*(h*l)+(b*l)
#area2=2*(h*l)
#area3=b*l
#area=area1+area2+area3
sqft=area/10.76391041671
paint=sqft*0.150

print("area of your room is:",sqft,"sqft")
print("you will need ",paint,"liters of paint")