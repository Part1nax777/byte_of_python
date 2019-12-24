def printMax(a,b):
  if a < b:
    print(a, 'минимально')
  elif a == b:
    print(a, 'равно', b)
  else:
    print(a, 'максимально')

printMax(4,5)
printMax(4,4)
printMax(5,4)

x = 4
y = 8
printMax(x, y)
