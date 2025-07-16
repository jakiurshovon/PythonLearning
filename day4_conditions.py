# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"Even number")
# else:
#     print(f"Odd number")
    
# if number < 0:
#     print(f"Negative number")   
# elif number > 0:
#     print(f"Positive number") 
# else:
#     print(f"Zero number") 

marks = int(input("Please input the marks: "))

if 0 <= marks <= 100:
    if marks >= 80:
        print("Grade: A+")
    elif marks >= 70:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: A-")
    elif marks >= 50:
        print("Grade: B")
    elif marks >= 40:
        print("Grade: C")
    else:
        print("Grade: Fail")
else:
    print("Please input marks between 0 and 100")
      
