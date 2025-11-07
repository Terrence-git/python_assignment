name=input("Enter your name") 
age=int(input("Enter your age"))

if age<12:
    fee=100
elif age>12 and age <18:
    fee=200
else:
    fee=300

print(f"{name} pays {fee}KES for admission")
