number = 23
guess = int(input('Введите число: '))

if guess == number:
  print('Вы угадали')
elif guess < number:
  print('Число больше')
else:
  print('Число меньше')

