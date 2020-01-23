import os
import time
import zipfile

source = [r"C:\Users\mSRychkov\Pictures", r"C:\Users\mSRychkov\Documents"]
target_dir = r"C:\Users\mSRychkov\Desktop"

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('Введите комментарий ->> ')

if len(comment) == 0:
  target = today + os.sep + now + '.zip'
else:
  target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
  os.mkdir(today)
  print('Каталог успешно создан', today)
zip_command = "python -m zipfile -c {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
  print('Резервная копия успешно создана', target)
else:
  print('Создание резервной копии не удалось')
