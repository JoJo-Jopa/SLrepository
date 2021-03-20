n = int(input())
for i in range(1, n):
    if i % 3 == 0 and i % 5 == 0:
        print("FillBuzz")
    elif i % 5 == 0 and i % 2 != 0:
        print("Buzz")
    elif i % 3 == 0 and i % 2 != 0:
        print("Fizz")
    elif i % 2 != 0:
        print(i)
# SLrepository
