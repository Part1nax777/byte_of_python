shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
print('Я должен сделать', len(shoplist), 'покупок')

def output(message):
  print(message, end= ' ')
  for item in shoplist:
    print(item, end=' ')

output('Покупки:')

print('\nТакже нужно купить немного риса')
shoplist.append('рис')

output('Теперь список покупок таков:')

print('Отсортирую ка я свой спиок:')
shoplist.sort()

output('Отсортированный список выглядит так:')

print('Первое что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил:', olditem)

output('Теперь мой список выглядит так:')
