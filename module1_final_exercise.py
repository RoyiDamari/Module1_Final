# conditions
# Exercise 1
x, y = map(float, input("Please enter 2 decimal numbers: ").split());
if x < y:
    print(x, x, x);
else:
    print(y, y, y);

# Exercise 2
a, b = map(int, input("Please enter 2 numbers: ").split());
print((x+y) / 2);

# Exercise 3
num1, num2, num3 = map(int, input("Please enter 3 numbers: ").split());
if num1 >= num2 and num1 >= num3:
    print(num1);
elif num2 >= num1 and num2 >= num3:
    print(num2);
else:
    print(num3);

# Exercise 4
movie_len: int = int(input("Please enter the movie length in minutes: "))
hours: int = movie_len // 60;
minutes: int = movie_len - (hours * 60);
print(f"The movie length is {hours} hours and {minutes} minutes");

# Exercise 5
num: int = int(input("Please enter a number with 4 digits: "));
last_digit: int = num % 10;
print(last_digit);

# Exercise 6
number: int = int(input("Please enter a number with 4 digits: "));
third_digit: int = (number // 10) % 10;
print(third_digit);

# Exercise 7
num: int = int(input("Please enter a number with 2 digits: "));
x: int = num % 10;
y: int = num // 10;
print(x + y);

# Exercise 8
num: int = int(input("Please enter a number with 2 digits: "));
x: int = num % 10;
y: int = num // 10;
print(f"{x}{y}");

# Exercise 9
num: int = int(input("Please enter a number with 2 digits: "));
if num % 2 == 0:
    print("Even number");
else:
    print("Odd number");

# Exercise 10
salary: int = int(input("Please enter your salary: "));
tax: float = 0;
if salary <= 6000:
    tax = 0 * salary;
elif salary <= 12000:
    tax = 0.1 * (salary - 6000);
elif salary <= 18000:
    tax = 0.2 * (salary - 12000) + 0.1 * (12000 - 6000);
elif salary <= 25000:
    tax = 0.3 * (salary - 18000) + 0.2 * (18000 - 12000) + 0.1 * (12000 - 6000);
elif salary <= 35000:
    tax = (0.4 * (salary - 25000) + 0.3 * (25000 - 18000) + 0.2 * (18000 - 12000)
           + 0.1 * (12000 - 6000));
elif salary <= 50000:
    tax = (0.45 * (salary - 35000) + 0.4 * (35000 - 25000) + 0.3 * (25000 - 18000)
           + 0.2 * (18000 - 12000) + 0.1 * (12000 - 6000));
else:
    tax = (0.5 * (salary - 50000) + 0.45 * (50000 - 35000) + 0.4 * (35000 - 25000)
           + 0.3 * (25000 - 18000) + 0.2 * (18000 - 12000) + 0.1 * (12000 - 6000));
print("The tax you have to paid is:", tax);

# Exercise 11
age: int = int(input("Please enter your age: "));
height: int = int(input("Please enter your height: "));
if age >= 18:
    if height >= 110:
        print("You can enter");
    else:
        print("You can't enter");
elif age >= 8:
    if height >= 115:
        print("You can enter");
    else:
        print("You can't enter");
else:
    print("You can't enter");

# Loops
# Exercise 1
number: int = int(input("Please enter a number: "));
i: int = 1;
for i in range(number + 1):
    print(i, end=" ");

# Exercise 2
num_1, num_2 = map(int, input("Please enter 2 numbers: ").split());
i: int = 0;
if num_1 < num_2:
    for i in range(num_1, num_2 + 1):
        print(i, end=" ");
else:
    for i in range(num_2, num_1 + 1):
        print(i, end=" ");

# Exercise 3
number: int = int(input("Please enter a number: "));
i: int = 0;
for i in range(i, number + 1, 2):
    print(i, end=" ");

# Exercise 4
den, maximum = map(int, input("Please enter 2 numbers: ").split());
i: int = 0;
for i in range(maximum + 1):
    if i % den == 0:
        print(i, end=" ");

# Data processing
# Exercise 1
user_input: bool = False
total: int = 0;
while True:
    number: int = int(input("Please enter a number: "));
    if number == -99:
        break

    total += number;
    user_input = True;

if user_input:
    print("The sum of the numbers is:", total);
else:
    print(None)

# Exercise 2
numbers: list[int] = [];
while True:
    number = int(input("Please enter a number: "));
    if number <= 0:
        break;

    numbers.append(number);

if numbers:
    max_value: int = max(numbers);
    min_value: int = min(numbers);
    print(f"The max value entered is: {max_value}");
    print(f"The min value entered is: {min_value}");
else:
    print("None")

# Exercise 3
numbers: list[int] = [];
for i in range(5):
    num: int = int(input("Please enter a number: "));
    numbers.append(num);
print(numbers);
max_number: int = max(numbers)
print(max_number);
max_index: int = numbers.index(max_number)
print(max_index);

# Exercise 4
x, y = map(int, input("Please enter 2 decimal numbers: ").split());
i: int = 1;
total: int = 0;
for i in range(y):
    total += x
print(total);

# Exercise 5
a, b = map(int, input("Please enter 2 numbers: ").split());
i: int = 1;
total: int = 1;
for i in range(b):
    total *= a
print(total);

# Exercise 6
check: bool = False;
num1, num2 = map(str, input("Please enter 2 numbers: ").split());
if num2 in num1:
    print(True);
else:
    print(False);

# Exercise 7
x, y = map(int, input("Please enter 2 numbers: ").split());
a: int = x;
b: int = y;
while b != 0:
    remainder = a % b;
    a = b;
    b = remainder;

print(f"The greatest common divisor of {x} and {y} is: {a}");

# Exercise 8
check: bool = False
num: int = int(input("Please enter a number: "));
for i in range(2, num):
    if num % i == 0:
        check = True

if check:
    print("This is not a prime number");
else:
    print("This is a prime number");

# Advanced loops
# Exercise 1
import statistics
temp_list: list[float] = [];
i: int = 0;
avg_temp: float = 0;
max_temp: float = 0;
min_temp: float = 0;

while i < 12:
    temp: float = None;
    while not temp:
        try:
            temp = float(input("Please enter a temperature: "));
            if temp == 0:
                break;

        except Exception as e:
            print(f"Something went wrong ---{e}---...try again")

    if temp < -5 or temp > 40:
        print("Wrong data");
        break;

    elif temp == 0:
        if temp == temp_list[i - 1]:
            continue;
        else:
            print("Correct data");
            temp_list.append(temp);

    else:
        print("Correct data");
        temp_list.append(temp);

    i += 1;

else:
    avg_temp = statistics.mean(temp_list);
    max_temp = max(temp_list);
    min_temp = min(temp_list);
    print(f"The temperature list is: {temp_list}");
    print(f"The average temperature is: {avg_temp}");
    print(f"The maximum temperature is: {max_temp}");
    print(f"The minimum temperature is: {min_temp}");

# Exercise 2
subject: str = input("Please enter the subject of the vote: ");
vote_list: list[int] = [];
i: int = 0;
count_vote_for: any = None;
count_vote_against: any = None;
count_abstained: any = None;
first_vote_for: any = None;
last_vote_against: any = None;

while i < 44:
    vote: int = None;
    while not vote:
        try:
            vote = int(input("Please enter your vote number: "));
            if vote < 1 or vote > 4:
                break;

        except Exception as e:
            print(f"Something went wrong ---{e}---...try again")

    if vote == 4:
        vote_list.append(vote);
        print("The country number that voted veto is: ", vote_list[i]);
        break;

    elif vote < 1 or vote > 4:
        continue;

    else:
        vote_list.append(vote);

    i += 1;

else:
    count_vote_for = vote_list.count(1);
    count_vote_against = vote_list.count(2);
    count_abstained = vote_list.count(3);
    first_vote_for = vote_list.index(1);
    last_vote_against = len(vote_list) - 1 - vote_list[::-1].index(2)
    print(f"The countries voted list is: {vote_list}");
    print(f"The number of countries voted for is: {count_vote_for}");
    print(f"The number of countries voted against is: {count_vote_against}");
    print(f"The number of countries that abstained from voting is: {count_abstained}");
    print(f"The first index number of the country voted for is: {first_vote_for}");
    print(f"The last index number of the country voted against is: {last_vote_against}");

