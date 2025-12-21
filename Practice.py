def func(a, b, c):
   print("This is function", a, "this is function", b, c)

func(1, 2, 3)

def len_list(list):
    s = print(len(list))
    return s


len_list([1, 2, 3])

# Function to check Odd/Even
def even_odd(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
    return n


even_odd(336)
even_odd(33)

# Conditional Operations
number = 15
result1 = not (number >= 1 and number <= 10)
result2 = (not number >= 1) or (not number <= 10)

print(result1)  # True
print(result2)  # True
print(True or True and False)
print(True and False)

# Age needs to reach till 120
age = int(input())
x = print(f"{120-age} years till 120")

a = 1
b = 0
c = a or b
if a == True:
    print("T")
else:
    print("F")

number = 9
power_of_two = 2

while power_of_two <= number:
    power_of_two *= 2

print(power_of_two)

num = float(input())

while num >= 3.5:
    num = num / 2
print(num)

print(7*"raj ")


for i in range(1, 21):
    if i % 2 == 1:
        continue
    print(i)


count_even = 0
for i in range(10, 51, 2):
    if i % 2 == 0:
        count_even += 1

print(f"count_even = {count_even}")


mult = 1
user = int(input())
for i in range(1, user + 1):
    mult *= i
print(mult)


start = 1
end = 10
step = 2
# Write your for loop here
for i in range(start, end, step):
    print(i)
for i in range(30, 81):
    if i % 4 == 0:
        print(i, end=",")
print("\n")
for i in range(15, 31, 2):
    print(i, end=",")
print("\n")
for i in range(50, 11, -5):
    print(i, end=",")
print("\n")
mult = 1
for i in range(1, 31, ):
    if i % 3 == 0:
        mult *= i
print(mult)

n = int(input())
# Write your code below
for i in range(1, n+1):
    for j in range(1, n+1):
        if i * j == n:
            print(i, j)


n = 3
res = 0
for i in range(n):
    a = 2
    res += a
print(res)

def hello_function():
    print("Hello Function!")


n = 5
# Write your code below
for i in range(n):
    hello_function()

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input('>')
print('Thank you!')

l = [1, 2, 3]
l.extend([9, 10])
print(l)

name = input("->").strip("asha")
print(name)

def Coconut_Capacity(number):
    calories = number+9
    yield calories
    print("Super")


a = Coconut_Capacity(9)
print(a)

for i in a:
    print(i)

name = input("name please? ")
colour = input("colour please? ")
print(name + " likes " + colour)

course = "pyhton"
print(course.replace("p", "ji"))

import getpass

password = getpass.getpass("Enter your password: ").strip()
print("You entered:", password)

print("Welcome to FizzBuzz!")
def FizzBuzz(num):
    for num in range(1,num+1):
        if '3' in str(num) and num%3 != 0 and num%7 != 0:
            print("Almost Fizz")
        elif num%3 == 0 and num%7 == 0:
            print("FizzBuzz")
        elif num%3 == 0:
            print("Fizz")
        elif num%7 == 0:
            print("Buzz")
        else:
           print(str(num))

FizzBuzz(int(input()))

shopping_list = ['bread', 'eggs', 'milk', 'butter']
print(f"shopping_list = {shopping_list}")

def values(lst):
     # Write code here
    Sum_list = 0
    for i in range(len(lst)):
        Sum_list = lst[i] + Sum_list
    print(Sum_list)


values([42])

#List Operations
def change_element(lst, index, lst2):
    # Write code here
    lst[index] = lst2[0]
    print(lst)

change_element([10, 20, 30, 40], 3, [99])

def merge(lst1, lst2):
    # Write code here
    lst1 = lst1 + lst2
    lst1.sort()
    print(lst1)


merge([9, 8, 7, 6, 5],[4, 3, 2, 1])

def combine_and_filter(lst, threshold):
    for element in lst:
        if element <= threshold:
            lst.pop()


    print(lst)


combine_and_filter([1, 5, 3, 2, 7, 4], 3)

def prod(lst):
    # Write code here
    mult = 1
    for elements in lst:
        mult = mult*elements
    print(mult)


prod([1, 4, 4, 2, 4, 98])

def reverse(lst):
    # Write code here
    lst.reverse()
    print(lst)

reverse([1,2,3])

lst = input().split(",")
# Write your code below
gt5_chars = []
for char in lst:
    if len(char) > 5:
        gt5_chars.append(char)
print(gt5_chars)

lst = list(map(int, input().split(",")))
# Write your code below
index_list = []
for index, val in enumerate(lst):
    if val < 50:
        index_list.append(index)
    elif val >= 50 and val % 5 == 0:
        index_list.append(index)
print(index_list)

numbers = input().split(',')
    # Write your code below
even_sum = 0
for val in numbers:
    if int(val) % 2 == 0:
        even_sum = even_sum + int(val)
print(even_sum)

lst = input().split()
# Write your code below
req_list = []
for index, val in enumerate(lst):
    if len(val) > 3 or val.startswith('a'):
        req_list.append(index)
print(req_list)

text = input().lower()
p_count = 0
for i in text:
    if i == "p":
        p_count = p_count + 1
print(p_count)

text = input()
s_count = 0
for i in text.lower():
    if i == "s":
        s_count = s_count + 1
print(s_count)

text = input()
delimiter = input()

new_list = text.split()
print(new_list)
new_text = delimiter.join(new_list)
print(new_text)

numbers = input()
prefix = input()
# Write your code below
new_numbers = numbers.split()
print(new_numbers)
print(" ".join(prefix + num for num in new_numbers))
prefix_number = prefix.join(new_numbers)
print(prefix_number)

lst = input().split(",")
# Write your code below
mid = len(lst) // 2
if len(lst) == 1:
    print(lst)
elif len(lst) % 2 == 0:
    middle_items = [lst[mid - 1], lst[mid]]
else:
    middle_items = [lst[mid - 1], lst[mid], lst[mid + 1]]
print(middle_items)

print(middle_items)

lst = input().split(",")

mid = len(lst)//2
print(lst[1::3])
print(lst[5::-1])
print(lst[mid::2])


def create_pattern(numbers, repeats):
    # Write your code here
    lst = numbers + numbers
    lst = lst * repeats
    print(lst)

create_pattern([3, 3, 3],5)

original_list = input().split(',')
# Write your code below
list1 = original_list[2::4]
list2 = original_list[2:len(original_list)-2]
list3 = original_list[-1::-2]
list4 = original_list[0:3] + original_list[-3:]

# Don't change below this line
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)

lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below
output_list = []
for element in lst1:
    if element not in lst2:
        output_list.append(element)
print(output_list)

input_list = input().split(', ')
# Write your code below
if len(input_list) >= 5:
    print(input_list[:2] + input_list[len(input_list)-2:])
else:
    print(list((input_list[0], input_list[-1])))

def not_mutual_friends(list1, list2):
    # Write your code below
    output_list = set(list1,list2)
    print(output_list)
list1 = input().split(",")
list2 = input().split(",")


not_mutual_friends(list1, list2)

for i in range(1, 11):
    if i == 7:
        continue
    print(i)

n = int(input())

for ele in range(1,n+1):
    if ele%2 == 0:
        continue
    else:
        print(ele*"*")


radius = float(input())
PI = 3.14159
area = PI * radius ** 2
print(area)

name, age, city = "Alice", 30, "New York"
x = y = z = 100
colors = ["red", "green", "blue"]
color1, color2, color3 = colors

print(f"Name: {name}, Age: {age}, City: {city}")
print(f"x: {x}, y: {y}, z: {z}")
print(f"Colors: {color1}, {color2}, {color3}")

def create_student_dict(name, age, major):
    # Write code here
    student_dict = {
        "name": name,
        "age": age,
        "major": major
    }
    print(student_dict)
    name = input()
    age = int(input())
    major = input()


create_student_dict()

def calculate_discount(price, discount_percentage):
    # Write code here
    discount_amount = price * (discount_percentage / 100)
    price = price - discount_amount
    print(round(price, 2))

calculate_discount(89.95,7)

def update_employee_info(employee_dict, key, value):
    # Write code here
    employee_dict[key] = value
    print(employee_dict)

update_employee_info({},"name","Eve")

recipe_book = {
    "Pancakes": ["flour", "milk", "eggs", "sugar"],
    "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
}
print(recipe_book["Pancakes"])
recipe_book["smoothie"] = ["banana", "milk", "honey"]
recipe_book["smoothie"].append("blueberries")
print(recipe_book)

def get_capital(country_capitals, country_name):
    # Write code here
    print(country_capitals[country_name])

def create_packing_list(traveler_name, days_per_location):
    # Write code here
    total_days = sum(days_per_location)
    print(f"Packing list for {traveler_name}:")
    print(f"- Clothes for {total_days} days \n- Toiletries")
    if total_days > 7:
        print("- Extra shoes")
    if total_days > 10:
        print("- Laundry soap")


create_packing_list("Bob", [4,2,1,6,3])

def create_book_dict(title, author, year):
    # Write code here
    book_dictionary =   {
        "title": title,
        'author': author,
        'year': year
    }
    print(book_dictionary)

    
create_book_dict(1984,"George Orwell",1949)

items = ["a", "b", "c", "d"]
print(len(items))

for i in range(len(items)):
    print(i, items[i])


student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
print(student_scores.get('David', "i don't give"))

def print_product_details(product_data):
    # Write code here
    if len(product_data) == 0:
        print("No product information available")
    else:
        for key, value in product_data.items():
            print(f"{key.capitalize()}: {value}")

def frequency_counter(data_list):
    frequency_dict = {}
    for item in data_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

def organize_camping_inventory(supplies):
    # Write code here
    req_items = sorted(supplies)
    for index,i in enumerate(req_items):
        print(f"Item #{index+1}: {i}")
    tinned_meat_count = supplies.count("tinned_meat")
    print(f"Tinned meat count: {tinned_meat_count}")


organize_camping_inventory(["water_bottle", "compass", "rope", "tinned_meat"])

def create_adoption_record(cats, dogs, location, contact):
    # Write code here 
    pets = cats + dogs
    print(f"Pets: {pets} | Location: {location} | Contact: {contact}")


create_adoption_record(["Tiger", "Leo", "Nala", "Simba"],["Rex",],"International Shelter", "000-0000-0000")

# Ternary Operator - One line If else statement
score = int(input())
status = "Pass" if score >= 50 else "Fail"
print(status)

names = ["Alice", "Bob", "Charlie"]
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

temperature = float(input())
warning = "Hot" if temperature > 30 else "Normal"
print(warning)

# Given data
names = ["Alice", "Bob", "Charlie"]
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
# Write code here
if "Alice" in names:
    print("Alice is in the list.")
if "David" not in names:
    print("David is not in the list.")
if "Bob" in grades:
    print("Bob is in the dictionary.")
if "Eve" not in names:
    print("Eve is not in the dictionary.")

def check_inventory(products, quantities):
    if "Apples" in products:
        print("Apples are in stock.")
    if "Oranges" not in products:
        print("Oranges are not in stock.")
    if "Bananas" in quantities:
        print("Bananas quantity is tracked.")
    if "Grapes" not in quantities:
        print("Grapes quantity is not tracked.")

check_inventory(["Cherries","Oranges","Watermelons","Apples"],{"Pears":15,"Cherries":40,"Apples":25})

