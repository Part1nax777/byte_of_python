ab = {  'Swaroop': 'swaroop@swaroopth.com',
        'Larry': 'larry@world.com',
        'Matsumoto': 'matz@ruby-lang.org',
        'Spammer': 'spammer@hotmail.com'
      }

print('Адрес swaroop:', ab['Swaroop'])
del(ab['Spammer'])
print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, address in ab.items():
  print('Контакт {0}, с адресом {1}'.format(name, address))

ab['Guido'] = 'guido@python.com'
if 'Guido' in ab:
  print('\nАдрес Guido:', ab['Guido'], '\n')

