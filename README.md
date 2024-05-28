МОИ СЛОВА
===============================================

Персональный словарь
--------------------
Предназначен для самостоятельного внесения новых слов во время изучения иностранного языка. В словаре предусмотрена
возможность тренировки, которая состоит в переводе слов, которые рандомно выбираются из вашего словаря. Слова могут иметь
несколько переводов. Также имеется функция учета вашего прогресса.


***Задача этого GUI – быть альтарнативой карточкам со словами, и служить эффективным инструментом пополнения своего 
словарного запаса иностранных слов.***



Написан с использованием
* *Python 3.7*
* *PyQt5*
* *Sql(QSqlQuery)*

Установка проекта
-----------------
Порядок установки проекта стандартный, самый быстрый способ:
- `cd "имя папки, где вы будете хранить клон проекта"`
- `git clone https://github.com/Ilysikov/My_words.git`

Настройка проекта
------------------
* Создайте виртуальное окружение. 
- `python3 -m venv "имя вашего окружения"`
- `source "имя вашего окружения"/bin/activate`

* Установите во вновь созданное окружение PyQt5, например, с помощью команд:
- `cd "имя вашего окружения"`
- `pip install pyqt5`

* Настройте "if__name__.py", как точку входа, если хотите увидеть работу GUI. 

* Для запуска тестов измените конфигурацию интерпретатора на "Unitest".

Сборка проекта
--------------
Проект можно преобразовать в исполняемый файл .exe с помощью PyInstaller:
* Установите pyinstaller: 
- `pip install pyinstaller`
- `cd "имя директории, в которой вы храните скрипт"`
- `pyinstaller --noconsole --onefile "имя файла"`

Краткое описпние работы GUI со стороны пользователя
---------------------------------------------------
В приожении есть три режима работы:
* Добавление нового слова
* Тренировка
* Редактирование

**Начальный режим – "Редактирование":**
![редактирование]( https://github.com/Ilysikov/My_words/raw/master/docs/static/redact.png)
Пользователю представляется таблица со словами, которые он добавлял. 
У таблицы четыре столбца: слово, которое пользователь запоминает, его перевод, его транслитерация
и транскрипция. Таблица поддерживает редактирование, а также запись в столбце перевод нескольких переводов.

**Тренировка**
![тренировка](https://github.com/Ilysikov/My_words/raw/master/docs/static/training.png)
В режиме тренировке пользователю предлаегается слово, перевод которого он вписывает в поле для ввода. Слова выводятся
рандомным образом. Тренировка поддерживается на обоих языках. Возможно несколько переводов одного слова. Так же в GUI 
предусмотрена функция счета прогресса. Если пользователь может правильно перевести слово с английского на русский, и с
русского на английский, его ему засчитывается знание одного слова. Прогресс рассчитавается в соответствии с 
общеизвестными стандартами уровня владения языка.

**Добавление нового слова:**
![добавить новое слово](https://github.com/Ilysikov/My_words/raw/master/docs/static/save.png)
Добавление новых слов намеренно реализовано, как отдельный режим ради, 
чтобы максимально ускорить ввод в условиях урока.

Структура прокта
----------------
* Ui_MainWindow.py – содержит скрипт отвечающий за граффический интерфейс основного окна.
* logika.py – состоит из несколько наследуемых классов, которые реализуют сценарии работы с приложением.
* SQL_tab.py – содержит реализацию взаимодействия с БД.
* if__name__.py - запускает исполнение скрипта. 
* class_Text.py – одиозный класс, который хранит словарь и алгоритм генерации сообщений.
* Modal.py – ответственен за графический интерфейс модлального окна. 








