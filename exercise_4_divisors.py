num = int(input("Enter a whole number greater than zero: "))
set_num = range(1, num+1)
divisors = []
for element in set_num:
  if num%element == 0:
    divisors.append(element)
print(divisors)
