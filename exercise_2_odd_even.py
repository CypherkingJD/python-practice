number = int(input("Please provide me a natual number (therefore greater than 0): "))
odd_even_remainder = number % 2
if odd_even_remainder == 0:
  print("Your number was even!")
else:
  print("Your number was odd!")
