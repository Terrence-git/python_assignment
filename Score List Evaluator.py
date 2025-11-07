test_score_list=[65, 88, 42, 90, 73, 55]
above70=0
below70=0
for score in test_score_list:
    if score>70:
        above70+=1
    else:
        below70+=1
print("Scores above 70",above70 )
print("Scores below 70", below70)