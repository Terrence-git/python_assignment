1. Age Access Program
Write a program that:
Asks the user to enter their age.


If the user is above 18, print "Access granted — you receive a complimentary drink!"


If the user’s age is between 16 and 18, print "Access granted — enjoy a juice pack!"


If the user is below 16, print "Access denied — you’re too young!"


2. Admission fee calc
 
Ask the user to enter their age and convert it to an integer.
 Using conditional statements:
Ages below 12 pay 100 KES


Ages 12–18 pay 200 KES


Ages above 18 pay 300 KES
 Print the message:
 "<name> pays <fee> KES for admission."

3. Even or Odd Analyzer
Create a list of numbers from 1 to 10.
 Use a for loop to check each number:
Print "Even number: X" if it’s even.


Print "Odd number: X" if it’s odd.


(Use modulus % and if-else inside your loop.

4. Grade Classifier
Ask the user to input their test score (0–100).
 Then:
80–100 → "Excellent"


50–79 → "Good"


0–49 → "Needs Improvement"
 If the input is outside the valid range, print "Invalid score entered."


(Use chained conditions with elif)



5. Discount Program
Ask the user for:
Product name


Product price



If the price is:
Above 10,000 → Apply 20% discount


Between 5,000 and 10,000 → Apply 10% discount


Below 5,000 → No discount


Print:
The <product> now costs <discounted_price> after discount.

(Hint: Use arithmetic operators and formatted strings.)



6. Login Simulation
Set variables:
stored_email = "user@example.com"
stored_password = "12345"

Ask the user for their email and password.
 If both match, print "Login successful!", otherwise print "Invalid credentials!".



 7. Weekend Detector (match statement)
Ask the user to input a number between 1 and 7 (representing days of the week).
 Use a match-case statement:
1 → Monday


2 → Tuesday


…


5 | 6 | 7 → "Looking forward to the weekend!"
 If none match, print "Invalid day number."


 8. Collection Sorter
Create a list of 7 random integers.
 Use a loop to:
Print all numbers greater than 10


Skip (using continue) numbers less than or equal to 10
 After the loop, print the total number of values that were greater than 10.






9. Favorite Fruits (Nested Loop Challenge)
Given:
colors = ["red", "green", "yellow"]
fruits = ["apple", "banana", "pear"]

Write a nested for loop to print all color–fruit combinations in the format:
red : apple
red : banana
...

Then print the total number of combinations printed.


10. Membership Checker
Create a list ["jeep", "suv", "sedan"].
 Ask the user to enter a car name.
 Check:
If it’s in the list → print "We have that car type!"


If not → print "Sorry, not available."




11. Dictionary Access Validation
Given:
user_profile = {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "verified": False
}

Ask the user:
 "Has the user verified their account? (yes/no): "
 If "yes", update the dictionary to set "verified": True and print the updated dictionary.
 Otherwise, print "Verification pending."



 12. Login Attempts (while loop)
Set a maximum of 3 login attempts using a while loop.
 Each time:
Ask the user to input a password.


If correct ("pass123"), print "Access granted" and stop the loop.


If incorrect, print "Wrong password, try again".


After 3 failed attempts, print "Account locked."



13. Type Identifier
Ask the user to input any value.
 Check and print:
The raw input


Its data type after checking with isinstance() for int, float, or str.



14. Score List Evaluator
Given a list of test scores: [65, 88, 42, 90, 73, 55]
 Using a loop:
Count how many scores are above 70


Count how many are below or equal to 70
 Print both results after the loop.



15. Nested Data Lookup
Given:
myFamily = {
    "father": {"name": "John", "year": 1985},
    "mother": {"name": "Jane", "year": 1990}
}

Write a script that:
Asks the user to input "father" or "mother"


Prints the name and birth year of the selected family member.
 If the input is neither, print "Family member not found.”













