def add(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

def calculate_average(numbers):git add .

    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Calling functions: 5 and 3 are arguments
print("Sum:", add(5, 3))
print("Is 10 even?", is_even(10))
print("Average:", calculate_average([10, 20, 30]))