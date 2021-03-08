print("Please the enter the first whole number")
number=int(input())
print("Please enter the second whole number")
number1=int(input())
print("Please the third whole number")
number2=int(input())

even_numbers = 0
odd_numbers = 0 

if (number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if ( number1 % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (number2 % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

print("There were {} even and {} odd numbers.".format(even_numbers, odd_numbers))