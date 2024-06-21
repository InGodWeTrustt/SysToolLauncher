## Виртуальное окружение
В консоли командной строки нужно последовательно прописать две команды:
1. <code>python -m venv venv</code> - создание виртуального окружения
2. .\venv\Scripts\activate - активация виртуального окружения

В случае успешной активации в консоли командной строки должно появиться, например, такое: 
<code>(venv) PS C:\Users\UserName\Desktop\SysToolLauncher></code>

Посмотреть какие пакеты установлены сейчас <code>pip list</code>

Примерный вывод в консоли командной строки после выполнения предыдущей команды:
```
Package            Version
------------------ -------
pip                23.1.2
PySide6            6.7.2
PySide6_Addons     6.7.2
PySide6_Essentials 6.7.2
setuptools         65.5.0
shiboken6          6.7.2
```
## Принцип работы
1. Нужно сначала создать виртуальное окружение
2. Установить пакет
```
   pip install pyside6
```
4.  Открыть в проводнике дизайнер по такому пути: C:\Users\UserName\Desktop\SysToolLauncher\venv\Lib\site-packages\PySide6\designer.exe и в нем уже создать макет. Далее сохранить в виде ui_mainwindow.ui
5. Далее нужно преобразовать этот файл в питоновский следующим образом:
   pyside6-uic ui_mainwindow.ui > ui_mainwindow.py
Если возникнет ошибку при открытии файла основого питона main.py,  выполнить то, что указано в разделе "Ошибки и решения"

## Ошибки и решения
Если выдаст такую ошибку ( File "C:\Users\UserName\Desktop\SysToolLauncher\main.py", line 3, in <module>        
    from ui_mainwindow import Ui_MainWindow
SyntaxError: source code string cannot contain null bytes), то
нужно файл ui_mainwindow.py сохранить в кодировке "UTF-8"

