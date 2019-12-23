while True:
  s = input('Введите что нибудь: ')

  if s == 'выход':
    break
  if len(s) < 3:
    print('введено слишком мало символов')
    continue
  print('Введеная строка:', s)
