user_profile = {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "verified": False
}
Response=input("Has the user verified their account? (yes/no): ")
if Response=="yes":
     user_profile["verified"] = True
     print(user_profile)
else:
    print("Verification pending.")

