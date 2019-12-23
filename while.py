number = 23
running = True

while running:
  guess = int(input('Введите число: '))

  if guess == number:
    print('Угадал')
    running = False
  elif guess < number:
    print('Число больше')
  else:
    print('Число меньше')
