# variables

student_name = "asha"
roll_no = 2
score = 9.9
average = True


# string examples

course = "python"
print(len(course))
print(course[0])
print(course[-2])
print(course[0:4])

# Escape sequences

print("asha is learning \"python\"")

# formatting string

x = 2
y = 15
print(f"x:{x}, y:{y}")

x = input("enter name")
y = input("enter age")
print(f"name of the student {x} \nage of the student {y}")

# number functions +, -, %, **, /, //(round figure of division), round, abs

x = 10 ** 2
print(x)

x = 7/2
print(round(x))

x = -1.5
print(abs(x))

# type conversion

float_val = 2.1
int_val = 2
add_val = float(int_val)-float_val
print(add_val)

# conditional statements if, if else, if elif else, nested if

age = input("enter age")  # y= int(input("enter age "))
y = int(age)  # optional
if y < 18:
    print(" u r not eligible")
elif 18 <= y <= 60:
    print("eligible")
else:
    print("senior citizen")


lottery_num = int(input("enter lottery num "))
winning_numbers = [23, 45, 68, 77]
if lottery_num in winning_numbers:
    print("won")
else:
    print("lose")

# While loop

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

number = 100
while number > 0:
    print(number)
    number //= 2

    while True:
        command = input(">")
        print("ECHO", command)
    if command.lower() == "quit":
        break


# to find even numbers

count = 0
for i in range(1, 20):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"wehave {count} even numbers")

def sigma(n):
    n = 0
    for num in range(1,n+1):
        n += num
    return n

print(1%2)
l = [1,2,4]
for jk, i in enumerate(l):
    print(jk+1, i)

