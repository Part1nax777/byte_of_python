try:
	text = input('Введите что нибудь >>')
except EOFError:
	print('CTRL D')
except KeyboardInterrupt:
	print('CTRL C')
else:
	print('Вы ввели {0}'.format(text))
