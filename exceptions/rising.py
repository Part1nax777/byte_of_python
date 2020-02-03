class ShortException(Exception):
	def __init__(self, word, length):
		Exception.__init__(self)
		self.word = word
		self.length = length

try:
	text = input('Введите что нибудь:')
	if len(text) < 3:
		raise ShortException(len(text), 3)
except EOFError:
	print('EOF')
except ShortException as ex:
	print('ShortException: длина строки {0}; \
		ожидалось минимум {1}'.format(ex.word, ex.length))
else:
	print('не было исключений')

