import shutil, os
os.chdir('C:\\')
#copy file to another dir
shutil.copy('C:\\java\\ex\\spam.txt', 'C:\\java\\ex\\delicious')

shutil.copy('C:\\java\\ex\\spam.txt', 'C:\\java\\ex\\delicious\\spam2.txt')

#The shutil.copytree() call creates a new folder named bacon_backup with the same
#content as the original bacon folder
shutil.copytree('C:\\java\\ex', 'C:\\java\\ex_backup1')


