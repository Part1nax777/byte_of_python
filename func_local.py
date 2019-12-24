x = 50

def func(x):
  print('X равен', x)
  x = 20
  print('Переменная функции', x)

func(x)
print('Глобальная переменная', x)
