import random

num1 = random.randint(1 , 99)
num2 = random.randint(1 , 99)

q1 = int(input(f"What is {num1} + {num2}?"))
a1 = num1 + num2
print(f"{num1} + {num2} = {a1}")

if q1 == a1:
    print("Your Answer is Correct!")
    print("")
    print("*************************")
else:
    print("Your Answer is Incorrect!")
    print("")
    print("*************************")

num1 = random.randint(1 , 99)
num2 = random.randint(1 , 99)

q2 = int(input(f"What is {num1} - {num2}?"))
a2 = num1 - num2
print(f"{num1} - {num2} = {a2}")

if q2 == a2:
    print("Your Answer is Correct!")
    print("")
    print("*************************")
else:
    print("Your Answer is Incorrect!")
    print("")
    print("*************************")

num1 = random.randint(1 , 99)
num2 = random.randint(1 , 99)

q3 = int(input(f"What is {num1} x {num2}?"))
a3 = num1 * num2
print(f"{num1} x {num2} = {a3}")

if q3 == a3:
    print("Your Answer is Correct!")
    print("")
    print("*************************")
else:
    print("Your Answer is Incorrect!")
    print("")
    print("*************************")

num1 = random.randint(1 , 99)
num2 = random.randint(1 , 99)

q4 = int(input(f"What is {num1} / {num2}?"))
a4 = num1 / num2
print(f"{num1} / {num2} = {a4}")

if q4 == a4:
    print("Your Answer is Correct!")
    print("")
    print("*************************")
else:
    print("Your Answer is Incorrect!")
    print("")
    print("*************************")
