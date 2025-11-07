Any_value=input("Enter any value: ")
if Any_value.isdigit():
    Any_value = int(Any_value)
elif Any_value.replace('.', '', 1).isdigit():
    Any_value = float(Any_value)
else:
    Any_value = str(Any_value)
if isinstance(Any_value, int):
    print(Any_value)
    print("This is an interger")
elif isinstance(Any_value, float):
    print(Any_value)
    print("This is a float")
elif isinstance(Any_value, str):
    print(Any_value)
    print("This is a string")
else:
    print("Wrong number")

