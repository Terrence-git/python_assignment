login_attempts=3
attempts=0

correct_pass="pass123"
while attempts<login_attempts:
     password=input("Enter your password: ")
     if password==correct_pass:
        print("Acces granted")
        break
     else:
        attempts += 1
        print("Wrong password, try again.")
if login_attempts==attempts:
    print ("account locked")

 

    
    


