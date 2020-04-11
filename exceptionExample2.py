import traceback
try:
    raise Exception('Это сообщение об ошибке')
except:
    errorFile = open('C:\\java\\pythonfolder\\errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Информация о стеке вызовов была записана в файл errorInfo.txt')
