import sys, warnings

if sys.version_info[0] < 3:
	print('Необходимо установить версию Python старше 3', RuntimeWarning)
else:
	print('Версия корректна')
