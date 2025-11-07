myFamily = {
    "father": {"name": "John", "year": 1985},
    "mother": {"name": "Jane", "year": 1990}
}
select=input("Enter 'father' or 'mother': ")
if select in myFamily:
    print("Name:", myFamily[select]["name"])
    print("Birth Year:", myFamily[select]["year"])
else:
    print("Family member not found.")