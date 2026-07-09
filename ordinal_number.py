numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        ending="st"
    elif number == 2:
        ending="nd"
    elif number == 3:
        ending="rd"
    else:
        ending="th"
    print(f"{numbers}{ending}")

    #This is a Ordinal Number Program in Python
    