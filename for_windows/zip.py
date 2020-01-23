import os
import zipfile

file = r'C:\Users\mSRychkov\Desktop\маркировка\REST API ОФД - ЧЗ.pdf'
newzip = zipfile.ZipFile(r'C:\Users\mSRychkov\Desktop\маркировка.zip', 'w')
newzip.write(file)
newzip.close()

