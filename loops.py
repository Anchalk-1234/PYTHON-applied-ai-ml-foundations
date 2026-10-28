print("Numbers from 1 to 5 using a for loop:")
for number in range(1, 6):
    print(number)

print("\nMultiplication table:")
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\nCountdown using a while loop:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Done!")
