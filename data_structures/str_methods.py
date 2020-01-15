name = 'Swaroop'

if name.startswith('Swa'):
  print('Да, строка начинается на "Swa"')

if 'wa' in name:
  print('Да строка содержит строку "wa"')

if name.find('war') != -1:
  print('Да, она содержит строку "war"')

delimiter = '_*_'

mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))
