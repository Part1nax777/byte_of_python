import re

def reverse(text):
	return text[::-1]

def is_palindrom(text):
	return text == reverse(text)

something = input('Введите текст: ')
something = something.lower().split()
something = ''.join(something)
something = re.sub('\ |\?|\.|\!|\/|\;|\:', '', something)

if (is_palindrom(something)):
	print("Палиндром")
else:
	print("Не палиндром")
