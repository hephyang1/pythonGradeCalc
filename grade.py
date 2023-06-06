print("Enter Marks Obtained in Mathematics")
Matheamtics = int(input())
print("Enter Marks Obtained in Science") 
Science = int(input())
print("Enter Marks Obtained in English")
English = int(input())

Score = Matheamtics + Science + English
avg = Score/3

if avg>=90 and avg<=100:
    print("Your Grade is A")
elif avg>=80 and avg<90:
    print("Your Grade is B")
elif avg>=70 and avg<80:
    print("Your Grade is C")
elif avg>=60 and avg<70:
    print("Your Grade is D")

elif avg>=0 and avg<60:
    print("Your Grade is F")
else:
    print("Invalid Input!")