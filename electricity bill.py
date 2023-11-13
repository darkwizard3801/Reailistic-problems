from datetime import datetime, date, timedelta
from random import randint
units=float(input("enter the units of electicity consumed:"))
if(units<=100):
    rs=units*1.5
    fixed=25.00
elif(units<=200):
    rs=(100*1.5)+(units-100)*2.5
    fixed=50.00
elif(units<=300):
    rs=(100*1.5)+(200-100)*2.5+(units-200)*4
    fixed=75.00
elif(units<=350):
    rs=(100*1.5)+(200-100)*2.5+(300-200)*4+(units-300)*5
    fixed=100.00
else:
    rs=units*1.5
    fixed=1500.00
total=rs+fixed;
meter=25
charge=30
duty=45
totalper=total/100
per=totalper*12
gst=total+per
Tot=gst+meter+charge+duty
rand=randint(1000, 9999)
pre=randint(100, 999)
phase=randint(1,3)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
 
print("con. no: C#5763156",rand)
print("pre unit:",pre)
print("purpose:Domistic")
print("meter Status:OK")
print("Load:4KW")
print("phase:",phase)
print("Units:",units)
print("tariff:Lt-1A Dom")

print("\ndate and time:",dt_string)
due=now + timedelta(days=10)
duedate=due.strftime("%d/%m/%Y %H:%M:%S")
exp=now + timedelta(days=27)
expdate=exp1.strftime("%d/%m/%Y %H:%M:%S")
print("due Date:",duedate)
print("dis Date:",expdate)
print("    KSEB BILL")
print("\n----------------------\n")
print ("\n\n\n\nfixed charge:",fixed)
print ("Meter rent:",meter)
print ("GST:12%")
print ("Energy charges:",charge)
print ("Duty:45")
print ("Others:0")
print("\n----------------------\n")
print("Bill amound   ₹%.2f"%total,"/-")
print("\nPayable amound :₹",Tot,"/-")
print("\n----------------------\n")
print("      remaks      ")
print("security Deposit\n Interest refund\n")
print("RS:₹₹₹")
