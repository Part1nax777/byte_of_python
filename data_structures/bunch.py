bri = set(['Бразилия', 'Россия', 'Индия'])
print('{0} содержится в списке?'.format('Индия'),'Индия' in bri)
print('{} cодержится в списке?'.format('США'), 'США' in bri)

bric = bri.copy()
bric.add('Китай')
print('bric включает все значения bri:', bric.issuperset(bri))
print('bri включает все значения bric:', bri.issuperset(bric))

bri.remove('Россия')
print('Пересечение множеств bri и bric:', bri & bric)

