#data types

#strings
print("Hello"[4])
print("123" + "345")

#Integers
print(123 + 345)
123_345_567

#Float
3.1423

#Boolean
True
False

#Type error, type checking and type conversion
num_char = len(input("What's your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

a = 123
print(type(a))
print(70 + float("170.6"))
#Day2 exercise 1
two_digit_number = input("Type a two digit number")
first_digit= two_digit_number[0]
second_digit= two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)

#mathematical operations
3 + 4
7 - 3
3 * 2
6 / 3
print(2 ** 2)
print(3 * 3 + 3 / 3 - 3)

#Day2 exercise 2
height= input("enter your height in m.")
weight= input("enter your weight in kg")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

#number manipulation and string
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))
print(type(8 // 3))

score = 0
score-=1
print(score)

score = 0
height = 1.8
isWinning = True
#f-string
print(f"your score is {score}, your height is {height}, you're winning is {isWinning}" )

#Day2 exercise 3
age = input("What's your current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
week_remaining = years_remaining * 52
month_remaining = years_remaining * 12
message = f"You have {days_remaining} days, {week_remaining} weeks, {month_remaining}month left"
print(message)