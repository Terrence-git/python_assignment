score=(0,101)
score=int(input ("Enter your test score"))
if score >79 and score <100:
    print("Excellent")
elif score>49 and score <80: 
    print("Good")
elif score >0 and score <50:
    print("Needs Improvement")
else:
    print("Invalid score entered.")

