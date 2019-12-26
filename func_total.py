def total(initial = 5, *numbers, **keywords):
  count = initial
  for number in numbers:
    count += number
  for keyword in keywords:
    count += keywords[keyword]
  return count

print(total(10, 1, 2, 3, vegetables = 50, fruits = 100))
