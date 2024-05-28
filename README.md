.. personal_dictyonary documentation master file, created by
   sphinx-quickstart on Tue Mar 19 23:20:06 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

МОИ СЛОВА
===============================================

Персональный словарь
--------------------
Предназначен для самостоятельного внесения новых слов во время изучения иностранного языка. В словаре предусмотрена
возможность тренировки, которая состоит в переводе слов, которые рандомно выбираются из вашего словаря. Слова могут иметь
несколько переводов. Также имеется функция учета вашего прогресса.


Задача этого GUI – быть альтарнативой карточкам со словами, и служить эффективным инструментом пополнения своего словарного запаса иностранных слов.



Написан с использованием

Python 3.7

PyQt5

Sql(QSqlQuery)

Установка проекта
-----------------
Порядок установки проекта стандартный, самый быстрый способ:
* cd "имя папки, где вы будете хранить клон проекта"
* git clone https://github.com/Ilysikov/My_words.git

Настройка проекта
------------------
Создайте виртуальное окружение. Если вы используете Pycharm откройте настройки интерпритатора и добавьте новый, выбрав
при этом версию Python 3.7. Добавьте в папку .venv папку docs.
В консоли Вашего проекта выполните следующие команды:

cd .venv

pip install -r docs/requirements.txt

Настройте "if__name__.py", как точку входа, если хотите увидеть работу GUI. Для запуска тестов измените конфигурацию,
на "Unitest".

Сборка проекта
--------------
Проект можно преобразовать в исполняемый файл .exe с помощью PyInstaller:
* Установите pyinstaller: pip install pyinstaller
* cd "имя директории, в которой вы храните скрипт"
* pyinstaller --noconsole --onefile "имя файла"

Краткое описпние работы GUI со стороны пользователя
---------------------------------------------------
В приожении есть три режима работы:
* Добавить новое слово
*Тренировка
*Редактирование

Начальный режим "Редактирование":
![]( https://github.com/Ilysikov/My_words/raw/master/docs/static/redact.png)



