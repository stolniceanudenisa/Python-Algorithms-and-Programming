c_y = 2020
c_m = 10
c_d = 6
b_d = int(input("Day of birth: "))
b_m = int(input("Month of birth: "))
b_y = int(input("Year of birth: "))
print("Current date: ",c_d,"/",c_m,"/",c_y)
print("Birthdate: ",b_d,"/",b_m,"/",b_y)
if b_m > c_m:
    print("Age: ",c_y - b_y - 1)
else:
    print("Age: ",c_y - b_y)
