import os, platform, logging

if platform.platform().startswith('Windows'):
	logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
															os.getenv('HOMEPATH'), \
															'test.log')
	print("Сохраняем лог в", logging_file)
else:
	logging_file = os.path.join(os.getenv('HOME'), 'test.log')

	logging.basicConfig(level = logging.DEBUG, #включить отладочные сообщения debug info 
											format = '%(asctime)s : Line:%(lineno)d : %(levelname)s : %(message)s', #формат записи в лог 
											filename = logging_file, #куда пишем лог
											#filemode = 'w' #перезапись файла
											)

	logging.debug('Начало программы')
	logging.info('Какие то действия')
	logging.warning('Программа умирает')
	logging.error('В программе есть ошибки')
	logging.critical('Сбой программы')

