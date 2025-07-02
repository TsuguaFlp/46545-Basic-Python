score = int(input('Enter your score (0-100): '))
if 0 <= score <= 100:
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid score. Please enter a value between 0 and 100.")