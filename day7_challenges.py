#Challenge 1: Find the Largest of Three Numbers

# num1 = float(input("Enter 3 numbers:\n1st number: "))
# num2 = float(input("\n2nd number: "))
# num3 = float(input("\n3rd number: "))

# if num1 == num2 == num3:
#     print("All numbers are equal.")
# elif num1 > num2 and num1 > num3:
#     print(f"The largest number is: {num1}")
# elif num2> num1 and num2 > num3:
#     print(f"The largest number is: {num2}")
# else:
#     print(f"The largest number is: {num3}")    
          


#Challenge 2: Even/Odd Counter from 1 to N

# number = int(input("Enter a number: "))
# even_count = 0
# odd_count = 0
# for i in range(1,number+1):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"Even: {even_count}")
# print(f"Even: {odd_count}")


#Challenge 3: Simple Login   
# user = input("User Name: ").strip()
# passw = input("Password: ")

# if user.lower() == "user" and passw == "pass123":
#     print("Success!")
# else:
#     print("Invalid login")


#Challenge 4: Sum of Digits

# number = input("Enter a number: ")

# total = 0
# for digit in number:
#     total += int(digit)
# print(f"Sum of digits = {total}")    


#Challenge 5: FizzBuzz

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print(f"{i}")