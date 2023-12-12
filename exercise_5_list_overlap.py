a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
compared = []
if len(b) > len(a):
  for element1 in a:
    for element2 in b:
      if element1 == element2:
        compared.append(element1)
elif:
  for element2 in b:
    for element1 in a:
      if element2 == element1:
        compared.append(element2)
