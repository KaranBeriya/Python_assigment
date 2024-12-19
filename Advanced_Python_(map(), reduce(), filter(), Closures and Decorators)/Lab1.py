#Write a Python program to apply the map() function to
#square a list of numbers.

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(lambda num: num ** 2, numbers)

print("Original list:", numbers)

print()

print("Squared list:", list(squared_numbers))