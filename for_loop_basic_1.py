# 1. Basic
for i in range(0, 151):
    print(i)

# 2. Multiples of 5
for i in range(5, 1001, 5):
    print(i)

# 3. Counting the Dojo Way
for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")
    elif i % 5 == 0 and i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

# 4. Whoa that Sucker's Huge
sum = 0
for i in range(1, 500000, 2):
    sum += i
print(sum)

# 5. Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# 6. Flexible Counter
lowNum = 2
highNum = 20
mult = 2
for i in range(2, 20, 2):
    if i % 2 == 0:
        print(i)