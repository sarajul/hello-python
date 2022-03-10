sal = int(input("Enter your salary : "))

if sal >= 20000:
    hra = (sal*12)/100
    da = (sal*20)/100
    pf = (sal*12)/100
else:
    hra = 1800
    da = (sal*15)/100
    pf = (sal*12)/100

net_sal = sal + hra + da - pf
print("Net Salary of : " , net_sal)