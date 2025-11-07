day=7
day=int(input("Enter the No: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5 | 6 | 7 :
        print("Looking foward to the weekend!")
    case _:
        print("Invalid day number.")