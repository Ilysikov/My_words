from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import (
    QTableView,
    QGridLayout,
    QProgressBar,
    QMainWindow)
from class_Text import Text
from logika import (Input_new_word, Input_trenirovka, See_word, Transcrition, Search_prog, slc, Tran_tren, Trans_ter, Chang,
W_search,Canc, Focus_tran)

class Ui_MainWindow(QMainWindow):
    def __init__(self,MainWindow:QtWidgets.QMainWindow)->None:
        super().__init__()
        """
        создание экземпляров, классов отвечающих за логику 
        """
        self.my_clases()
        """
        создание и описание основного окна 
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setStyleSheet("background-color: rgb(208, 191, 191);")
        self.centralwidget.setObjectName("centralwidget")
        """
        создание и описание базового виджета
        """
        self.TabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(0, 0, 640, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabWidget.sizePolicy().hasHeightForWidth())
        self.TabWidget.setSizePolicy (sizePolicy)
        self.TabWidget.setMouseTracking(False)
        self.TabWidget.setTabletTracking(True)
        self.TabWidget.setAcceptDrops(False)
        self.TabWidget.setToolTip("")
        self.TabWidget.setAutoFillBackground(False)
        self.TabWidget.setStyleSheet("background-color: rgb(209, 193, 192);")
        self.TabWidget.setUsesScrollButtons(False)
        self.TabWidget.setDocumentMode(False)
        self.TabWidget.setMovable(False)
        self.TabWidget.setTabBarAutoHide(False)
        self.TabWidget.setObjectName("TabWidget")
        """
        создание вкладки в базовом виджете "Добавить новое слово" (далее – вкладка 1)
        """
        self.tabWidget_new_word = QtWidgets.QWidget()
        self.tabWidget_new_word.setObjectName("tabWidget_new_word")
        """
        создание переменных ссылающихся на текст в словаре класса "Text"
        """
        self.column=self.text_.c_text(key_='rus')
        self.column_chek=self.text_.c_text(key_='eng')
        self.columnask=self.text_.c_text(key_='R_rus')
        self.number=self.text_.c_text(key_='None')
        self.w=self.text_.c_text(key_='None')
        self.percent=self.text_.c_text(key_='r_percent')
        """
        лэйбл-фон во вкладке 1
        """
        self.label_2 = self.create_label_NT(label_name="label_2",
                                            geometry=QtCore.QRect(0, -40, 640, 501))
        self.label_2.setMouseTracking(False)
        self.label_2.setTabletTracking(False)
        self.label_2.setAcceptDrops(False)
        self.label_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_2.setText("")
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        """
        поле ввода во вкладке 1 для записи слова на Английском
        """
        self.lineEdit_NT_input_field_english = self.create_line(name="lineEdit_NT_input_field_english",
                                                                geometry=QtCore.QRect(0, 80, 640, 35),
                                                                tabwidget=self.tabWidget_new_word)
        self.lineEdit_NT_input_field_english.setToolTipDuration(-1)
        self.lineEdit_NT_input_field_russian = self.create_line(name="lineEdit_NT_input_field_russian",
                                                                geometry=QtCore.QRect(0, 160, 640, 35),
                                                                tabwidget=self.tabWidget_new_word)
        self.lineEdit_NT_input_field_transliteration = self.create_line(name="lineEdit_NT_input_field_transliteration",
                                                                geometry=QtCore.QRect(0, 240, 640, 35),
                                                                tabwidget=self.tabWidget_new_word)
        self.lineEdit_NT_input_field_transcrition = self.create_line(name="lineEdit_NT_input_field_transcrition",
                                                                geometry=QtCore.QRect(0, 320, 640, 35),
                                                                tabwidget=self.tabWidget_new_word)
        self.pushButton_NT_save = self.create_pushButton(but_name="pushButton_NT_save", 
                                                         tabwidget=QtWidgets.QPushButton(self.tabWidget_new_word), 
                                                        geometry=QtCore.QRect(450, 390, 151, 32))
        """
        лебл для комментария над полем для ввода слова на Английском
        """
        self.label_NT_str_03 = self.create_label_NT(label_name="label_NT_str_03")

        self.label_NT_str_04 = self.create_label_NT(label_name="label_NT_str_04",
                                                    geometry=QtCore.QRect(10, 200, 181, 21))
        self.label_NT_str_05 = self.create_label_NT(label_name="label_NT_str_05",
                                                    geometry=QtCore.QRect(10, 280, 391, 21))
        self.label_NT_str_06 = self.create_label_NT(label_name="label_NT_str_06",
                                                    geometry=QtCore.QRect(10, 360, 391, 21))
        """
        кнопка "Отмена"
        """
        self.pushButton_NT_cancel = self.create_pushButton(but_name="pushButton_NT_cancel", 
                                                           tabwidget=QtWidgets.QPushButton(self.tabWidget_new_word), 
                                                           geometry=QtCore.QRect(280, 390, 151, 32))
        """
        лэйбл для записи первой части инструкции
        """
        self.label_NT_str_01 = self.create_label_NT(label_name="label_NT_str_01",
                                                    geometry=QtCore.QRect(10, 15, 481, 21))
        self.label_NT_str_01.setTextFormat(QtCore.Qt.RichText)
        self.label_NT_str_02 = self.create_label_NT(label_name="label_NT_str_02",
                                                    geometry=QtCore.QRect(10, 35, 481, 21))
        self.label_NT_str_02.setTextFormat(QtCore.Qt.RichText)
        self.TabWidget.addTab(self.tabWidget_new_word, "")

        """
        создание и описание в базовом виджете вкладки "Тренировка" (далее – вкладка 2)
        """
        self.tabWidget_training = QtWidgets.QTabWidget()
        self.tabWidget_training.setObjectName("tabWidget_training")
        self.tabWidget_training.tabBarClicked.connect(self.clic_tren.chek_create)
        """
        поле для ввода ответа пользователя в процессе тренировки 
        """
        self.lineEdit_T_input_field = self.create_line(name="lineEdit_T_input_field",
                                                                geometry=QtCore.QRect(0, 200, 640, 50),
                                                                tabwidget=self.tabWidget_training)
        self.lineEdit_T_input_field.setToolTipDuration(10)
        self.lineEdit_T_input_field.setAutoFillBackground(False)
        """
        лейбл-фон для вкладки 2 
        """
        self.label_T = self.create_label(label_name="label_T",
                                              geometry=QtCore.QRect(0, -30, 645, 501))
        self.label_T.setMouseTracking(False)
        self.label_T.setTabletTracking(True)
        self.label_T.setAcceptDrops(False)
        self.label_T.setText("")
        """
        кнопка "Проверить"
        """
        self.pushButton_T_check = self.create_pushButton(but_name="pushButton_T_check",
                                                         tabwidget=QtWidgets.QPushButton(self.tabWidget_training), 
                                                         geometry=QtCore.QRect(490, 280, 113, 32))
        """
        кнопка переключения языка 1 (начальное положение кнопки – "Русский")
        """
        self.toolButton_T_rus = self.create_pushButton(but_name="toolButton_T_rus",
                                                       tabwidget=QtWidgets.QToolButton(self.tabWidget_training), 
                                                       geometry=QtCore.QRect(190, 10, 120, 25))
        """
        кнопка переключения языка 3 (начальное положение кнопки – "Английский")
        """
        self.toolButton_T_eng = self.create_pushButton(but_name="toolButton_T_eng",
                                                       tabwidget=QtWidgets.QToolButton(self.tabWidget_training), 
                                                       geometry=QtCore.QRect(350, 10, 120, 25))
        """
        кнопка переключения языка 2 – значок "<=>"
        """
        self.slider=self.create_pushButton(but_name="slider",
                                           tabwidget=QtWidgets.QToolButton(self.tabWidget_training), 
                                           geometry=QtCore.QRect(315, 10, 30, 25))
        """
        конпка "Тренироваться"/"Пропустить"
        """
        self.pushButton_T_skip = self.create_pushButton(but_name='pushButton_T_skip',
                                                        tabwidget=QtWidgets.QPushButton(self.tabWidget_training), 
                                                        geometry=QtCore.QRect(30, 280, 113, 32))
        # лэйбл для вывода слов, которые необходимо перевести в процессе тренировки
        self.label_T_word = self.create_label(label_name="label_T_word",
                                              stile='',
                                              geometry=QtCore.QRect(140, 70, 350, 40))
        self.label_T_word.setAlignment(Qt.AlignCenter)
        """
        лэйбл с комментарием над полем для пользовательского ввода
        """
        self.label_T_str_01 = self.create_label(label_name="label_T_str_01",
                                                geometry=QtCore.QRect(0, 170, 381, 31))
        """
        лэйбл для комментария о том, на каком языке будут выводиться слова
        """
        self.label_T_str_00 = self.create_label(label_name="label_T_str_00")
        """
        лэйбл "Ваш прогресс"
        """
        self.label_T_str_02 = self.create_label(label_name="label_T_str_02")
        """
        лэйбл с указанием уровня англиского 
        """
        self.label_T_str_03 = self.create_label(label_name="label_T_str_03")
        """
        лэйбл с транскрипцией и/или транслитерацией слова
        """
        self.label_T_str_04 = self.create_label(label_name="label_T_str_04")
        """
        лэйбл с количеством слов в словаре
        """
        self.label_T_str_05 = self.create_label(label_name="label_T_str_05")
        """
        шклала прогресса 
        """
        self.progress=QProgressBar(self.tabWidget_training)
        self.progress.setMaximum(100)
        """
        "raise_" поднимает виджет в вверх родительского виджета; 
        размещаю после создания взаимосвязанных виджетов, чтобы избежать ошибки 
        """
        self.label_T.raise_()
        self.lineEdit_T_input_field.raise_()
        self.pushButton_T_check.raise_()
        self.pushButton_T_skip.raise_()
        self.slider.raise_()
        self.toolButton_T_rus.raise_()
        self.toolButton_T_eng.raise_()
        self.label_T_word.raise_()
        self.label_T_str_01.raise_()
        self.label_T_str_02.raise_()
        self.label_T_str_00.raise_()
        self.label_T_str_03.raise_()
        self.label_T_str_04.raise_()
        self.label_T_str_05.raise_()
        self.progress.raise_()
        """
        добавление вкладки 2 к базовому виджету
        """
        self.TabWidget.addTab(self.tabWidget_training, "")
        """
        создание в базовом виджете вкладки "Редактирование" (далее - вкладка 3) 
        """
        self.tabWidget_edit = QtWidgets.QWidget()
        self.tabWidget_edit.setObjectName("tabWidget_edit")
        """
        создание графической таблицы, для отображения таблицы "words_"
        """
        self.model = QSqlTableModel(self.tabWidget_edit)
        self.model.setTable('words_')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ENGLISH")
        self.model.setHeaderData(1, Qt.Horizontal, "RUSSIAN")
        self.model.setHeaderData(2, Qt.Horizontal, "TRANSLIT")
        self.model.setHeaderData(3, Qt.Horizontal, "TRANSKRIP")
        self.model.select()
        """
        описание графической таблицы
        """
        self.view = QTableView(self.tabWidget_edit)
        self.view.setModel(self.model)
        self.view.setGeometry(QtCore.QRect(0, 0, 635, 420))
        self.view.setColumnWidth(0,160)
        self.view.setColumnWidth(1,160)
        self.view.setColumnWidth(2,140)
        self.view.setColumnWidth(3,140)
        self.view.setWordWrap(True)
        """
        добавление вкладки 3 к базовому виджету
        """
        self.TabWidget.addTab(self.tabWidget_edit,'')
        """
        размещение основного окна по центру 
        """
        MainWindow.setCentralWidget(self.centralwidget)
        """
        бегунок прокрутки
        """
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        """
        создание экземпляров классов отвечающих за логику, и их инициализация
        """
        self.inicial()
        """
        добавление к виджетам начального текста, отклики и пользовательский ввод 
        """
        self.retranslateUi(MainWindow)
        """
        установка начального виджета при входе
        """
        self.TabWidget.setCurrentIndex(2)
        """
        связывает родительские слоты с дочерними объектами
        """
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        """
        создание "сетки" для виджетов
        """
        btn_layout = QGridLayout(self.centralwidget)
        btn_layout_1 = QGridLayout(self.tabWidget_new_word)
        btn_layout_2 = QGridLayout(self.tabWidget_training)
        btn_layout_3=QGridLayout(self.tabWidget_edit)
        """
        привязка виджетов к "сетке" 
        """
        btn_layout.addWidget(self.TabWidget,0,0,0,0)
        btn_layout_1.addWidget(self.label_2,0,0,11,0)
        btn_layout_1.addWidget(self.label_NT_str_01,0,0,1,2)
        btn_layout_1.addWidget(self.label_NT_str_02,1,0,1,0)
        btn_layout_1.addWidget(self.label_NT_str_03,2,0,1,0)
        btn_layout_1.addWidget(self.lineEdit_NT_input_field_english,3,0,1,0)
        btn_layout_1.addWidget(self.label_NT_str_04,4,0,1,0)
        btn_layout_1.addWidget(self.lineEdit_NT_input_field_russian,5,0,1,0)
        btn_layout_1.addWidget(self.label_NT_str_05,6,0,1,0)
        btn_layout_1.addWidget(self.lineEdit_NT_input_field_transliteration,7,0,1,0)
        btn_layout_1.addWidget(self.label_NT_str_06,8,0,1,0)
        btn_layout_1.addWidget(self.lineEdit_NT_input_field_transcrition,9,0,1,0)
        btn_layout_1.addWidget(self.pushButton_NT_save,12,1,1,1)
        btn_layout_1.addWidget(self.pushButton_NT_cancel,12,0,1,1)
        btn_layout_2.addWidget(self.label_T,0,0,6,0)
        btn_layout_2.addWidget(self.toolButton_T_rus,0,1,1,1)
        btn_layout_2.addWidget(self.slider,0,2,1,1)
        btn_layout_2.addWidget(self.toolButton_T_eng,0,3,1,1)
        btn_layout_2.addWidget(self.label_T_str_00,0,0,1,1)
        btn_layout_2.addWidget(self.label_T_word,1,1,1,3)
        btn_layout_2.addWidget(self.label_T_str_01,2,0,1,0)
        btn_layout_2.addWidget(self.lineEdit_T_input_field,3,0,1,0)
        btn_layout_2.addWidget(self.pushButton_T_skip,6,0,1,1)
        btn_layout_2.addWidget(self.pushButton_T_check,6,4,1,1)
        btn_layout_2.addWidget(self.progress, 4,1,1,3)
        btn_layout_2.addWidget(self.label_T_str_02,4,0,1,1)
        btn_layout_2.addWidget(self.label_T_str_05,0,4,1,1)
        btn_layout_2.addWidget(self.label_T_str_03,4,4,1,1)
        btn_layout_2.addWidget(self.label_T_str_04,5,0,1,0)
        btn_layout_3.addWidget(self.view,0,0,0,0)
    
    def my_clases(self):
        """
        ниже класс иницирующий проверку введенного слова
        """
        self.clic_tren=Tran_tren(dict_word={'trenirovka':''})
        """
        отвечает за присвоение переменным текста 
        """
        self.text_=Text()
        """
        инициирует поиск слова в словаре, является родительским классом
        """
        count=W_search()
        """
        присваивается количество (int) слов в словаре
        """
        self.count_table=count.count_tab()
        """
        отвечает за отображение слов для перевода в процессе тренировки 
        """
        self.trenirovka=See_word()
    def inicial(self)->None:
        """
        методы экземпляров иницируются при соотвествующем сигнале,
        который определен в "retranslateUi"
        при создании передаются переменные хранящие объекты-виджеты
        Focus_tran отвечает за перемещение курсора при нажатии Enter
        """
        self.foc_e=Focus_tran(self.lineEdit_NT_input_field_english)
        self.foc_r=Focus_tran(self.lineEdit_NT_input_field_russian)
        self.foc_t=Focus_tran(self.lineEdit_NT_input_field_transliteration)
        self.foc_tran=Focus_tran(self.lineEdit_NT_input_field_transcrition)
        """
        Canc отвечает за очистку полей ввода
        """
        self.can_=Canc(list_=[self.lineEdit_NT_input_field_english, self.lineEdit_NT_input_field_russian,
              self.lineEdit_NT_input_field_transcrition, 
              self.lineEdit_NT_input_field_transliteration])
        """
        Trans_ter отвечает за передачу в другие классы пользовательского ввода (str)
        """
        self.ter=Trans_ter()
        """
        Input_new_word родительский класс отвечает за передачу пользовательского ввода 
        Trans_ter или его дочерним классам
        """
        self.new_tran=Transcrition(name='self.tran', class_obj=self.ter)
        self.new_e=Input_new_word(name='self.e', class_obj=self.ter)
        self.new_r=Input_new_word(name='self.r', class_obj=self.ter)
        self.new_t=Input_new_word(name='self.t', class_obj=self.ter)
        self.tren=Input_trenirovka(name='trenirovka', class_obj=self.clic_tren)
        """
        передаем в class slc переменные 
        """
        slc.po(pole_1=self.label_NT_str_01, pole_2=self.label_NT_str_02,
                            pole_3=self.label_T_str_05,pole_4=self.pushButton_T_skip,
                            pole_5=self.lineEdit_T_input_field,
                            pole_6=self.label_T_word,
                            pole_7=self.label_T_str_04,
                            pole_8=self.label_T_str_01,
                            pole_9=self.label_T_str_03,
                            pole_10=self.progress,
                            model=self.model)
        slc.percent_(percent=self.percent)
        slc.column_(column=self.column)
        slc.column_chek_(column_chek=self.column_chek)
        slc.columnask_(columnask=self.columnask)
        slc.ret1(list_=[self.lineEdit_NT_input_field_english, self.lineEdit_NT_input_field_russian,
              self.lineEdit_NT_input_field_transcrition, 
              self.lineEdit_NT_input_field_transliteration])
        """
        иницирует подсчет значений в таблице "progress_"
        """
        self.prog=Search_prog()
        self.prog.progress_()
        """
        присваивает значения необходимые для отображения слов в процессе тренировки
        """
        self.trenirovka.tran_column()
        self.trenirovka.count_tab()
        """
        передает значения 
        """
        self.text_.peremen_(col=self.columnask, label_T_str_00=self.label_T_str_00)
          
    def retranslateUi(self, MainWindow)->None:
        """
        метод translate возвращает перевод исходного текста
        """
        _translate = QtCore.QCoreApplication.translate
        """
        титул основного окна
        """
        MainWindow.setWindowTitle(_translate("MainWindow", "Учебный Словарик"))
        """
        поле для ввода слова на Английском
        """
        self.lineEdit_NT_input_field_english.setPlaceholderText(_translate("MainWindow", self.text_.c_text(key_="input")))
        """
        перемещение курсора при нажатии Enter
        """
        self.lineEdit_NT_input_field_english.returnPressed.connect(self.foc_r.foc_)
        """
        вызов метода Input_new_word и передача ему введенного текста
        """
        self.lineEdit_NT_input_field_english.textChanged.connect(self.new_e.new_w)
        """
        ввод на Руссом
        """
        self.lineEdit_NT_input_field_russian.setPlaceholderText(_translate("MainWindow", self.text_.c_text(key_="input")))
        self.lineEdit_NT_input_field_russian.returnPressed.connect(self.foc_t.foc_)
        self.lineEdit_NT_input_field_russian.textChanged.connect(self.new_r.new_w)
        """
        Транслитерация
        """
        self.lineEdit_NT_input_field_transliteration.setPlaceholderText(_translate("MainWindow", self.text_.c_text(key_="input")))
        self.lineEdit_NT_input_field_transliteration.returnPressed.connect(self.foc_tran.foc_)
        self.lineEdit_NT_input_field_transliteration.textChanged.connect(self.new_t.new_w)
        """
        Транскрипция
        """
        self.lineEdit_NT_input_field_transcrition.setPlaceholderText(_translate("MainWindow", self.text_.c_text(key_="input")))
        self.lineEdit_NT_input_field_transcrition.returnPressed.connect(self.foc_e.foc_)
        self.lineEdit_NT_input_field_transcrition.returnPressed.connect(self.ter.comand_serch)
        self.lineEdit_NT_input_field_transcrition.textChanged.connect(self.new_tran.new_w)
        """
        присваение текста и события кнопке "Сохранить"
        """
        self.pushButton_NT_save.setText(_translate("MainWindow", self.text_.c_text(key_="save")))
        self.pushButton_NT_save.clicked.connect(self.ter.comand_serch)
        """
        отображение в лейблах коментирующего текста
        """
        self.label_NT_str_03.setText(_translate("MainWindow", self.text_.c_text(key_="w_english")))
        self.label_NT_str_04.setText(_translate("MainWindow", self.text_.c_text(key_="w_russian")))
        self.label_NT_str_05.setText(_translate("MainWindow", self.text_.c_text(key_="w_translit")))
        self.label_NT_str_06.setText(_translate("MainWindow", self.text_.c_text(key_="w_transkrip")))
        """
        присваение текста и события кнопке "Отмена"
        
        """
        self.pushButton_NT_cancel.setText(_translate("MainWindow", self.text_.c_text(key_="cancel")))
        self.pushButton_NT_cancel.clicked.connect(self.can_.cancel_)
        """
        присваение текста инструкции (разделен на два лэйбла)
        """
        self.label_NT_str_01.setText(_translate("MainWindow", self.text_.c_text(key_="nt_1")))
        self.label_NT_str_02.setText(_translate("MainWindow", self.text_.c_text(key_="nt_2")))
        """
        текст заглавия вкладки 1
        """
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tabWidget_new_word),
                                  _translate("MainWindow", self.text_.c_text(key_="tab_widget_nt")))
        """
        поле ввода пользовательского ответа в процессе тренировки
        присвоен текст, события ввода и нажатия Enter
        """
        self.lineEdit_T_input_field.setPlaceholderText(_translate("MainWindow", self.text_.c_text(key_="input")))
        self.lineEdit_T_input_field.returnPressed.connect(self.clic_tren.chek_create)
        self.lineEdit_T_input_field.textChanged.connect(self.tren.new_w)
        """
        присваение текста и события кнопки "Проверить"
        """
        self.pushButton_T_check.setText(_translate("MainWindow", self.text_.c_text(key_="t_chek")))
        self.pushButton_T_check.clicked.connect(self.clic_tren.chek_create)
        """
        присваение текста и события кнопки "Тренироваться"/"Пропустить"
        """
        self.pushButton_T_skip.setText(_translate("MainWindow", self.text_.c_text(key_="t_skip")))
        self.pushButton_T_skip.clicked.connect(self.clic_tren.comand_see)
        """
        присваение текста и события 
        """
        self.toolButton_T_rus.setText(_translate("MainWindow", self.text_.c_text(key_="t_rus")))
        self.toolButton_T_rus.clicked.connect(self.text_.ask_)
        self.toolButton_T_eng.setText(_translate("MainWindow", self.text_.c_text(key_="t_eng")))
        self.toolButton_T_eng.clicked.connect(self.column_)
        self.slider.setText(_translate("MainWindow", self.text_.c_text(key_="slider_")))
        self.slider.clicked.connect(self.column_)
        self.label_T_word.setText(_translate("MainWindow", self.text_.c_text(key_='None')))
        self.label_T_str_00.setText(_translate("MainWindow", self.text_.c_text(key_='None')))
        self.label_T_str_01.setText(_translate("MainWindow", self.text_.c_text(key_="t_1")))
        self.label_T_str_02.setText(_translate("MainWindow", self.text_.c_text(key_="t_2")))
        self.label_T_str_05.setText(_translate("MainWindow", self.text_.i_text(key_='t_05',
                                                list_dic={'self.count_table':self.count_table})))
        self.label_T_str_04.setText(_translate("MainWindow", self.text_.c_text(key_='None')))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tabWidget_training), _translate("MainWindow", self.text_.c_text(key_='tab_widget_t')))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tabWidget_edit), _translate("MainWindow", self.text_.c_text(key_='tab_widget_r')))
        
    def column_(self)->None:
        """
        класс Chang отвечает за изменение значений переменных при переключении языка
        """
        self.col=Chang()
        """
        возвращает список с измененными значениями 
        """
        self.list_chang=self.col.colu_n(list=[self.column,self.toolButton_T_eng,
            self.toolButton_T_rus, self.pushButton_T_skip,
            self.label_T_word, self.lineEdit_T_input_field,
            self.label_T_str_01, self.columnask,
            self.label_T_str_00, self.column_chek,
            self.percent])
        """
        присваение некоторых значений
        """
        self.column=self.list_chang[0]
        self.columnask=self.list_chang[1]
        self.column_chek=self.list_chang[2]
        self.percent=self.list_chang[3]
        """
        передача переменных с новыми значениями другим классам 
        """
        self.text_.peremen_(col=self.columnask, label_T_str_00=self.label_T_str_00)
        slc.percent_(percent=self.percent)
        slc.column_(column=self.column)
        slc.column_chek_(column_chek=self.column_chek)
        slc.columnask_(columnask=self.columnask)
        self.trenirovka.tran_column()
        
    """
    метод возвращает новые лэйблы вкладки "Тренировка"
    """
    def create_label(self,label_name:str,
                        stile:str="background-color: rgb(225, 200, 191);", 
                        geometry:QtCore.QRect=QtCore.QRect(140, 50, 180, 20))-> object:
        label_T_str = QtWidgets.QLabel(self.tabWidget_training)
        label_T_str.setGeometry(geometry)
        label_T_str.setStyleSheet(stile)
        label_T_str.setInputMethodHints(QtCore.Qt.ImhNone)
        label_T_str.setWordWrap(False)
        label_T_str.setOpenExternalLinks(False)
        label_T_str.setObjectName(label_name)
        return label_T_str
    
    """
    метод возвращает новые кнопки
    из-за множества параметров данный метод не сокращает объем кода 
    """
    def create_pushButton(self, but_name:str,
                          tabwidget: object,
                          geometry: QtCore.QRect)-> object:
        pushButton=tabwidget
        pushButton.setGeometry(geometry)
        pushButton.setObjectName(but_name)
        return pushButton
    
    """
    метод возвращает новые лэйблы вкладки "Добавить новое слово"
    """
    def create_label_NT(self,label_name:str,
                        stile:str="background-color: rgb(178, 180, 186);", 
                        geometry=QtCore.QRect(10, 120, 181, 21))-> object:
        label_NT = QtWidgets.QLabel(self.tabWidget_new_word)
        label_NT.setGeometry(geometry)
        label_NT.setStyleSheet(stile)
        label_NT.setObjectName(label_name)
        return label_NT
    
    """
    метод возвращает новые поля для пользовательского ввода текста 
    """
    def create_line(self,geometry: QtCore.QRect, name: str, tabwidget: object,
                    style: str="background-color: rgb(208, 191, 191);")-> object:
        line_edit= QtWidgets.QLineEdit(tabwidget)
        line_edit.setGeometry(geometry)
        line_edit.setStyleSheet(style)
        line_edit.setDragEnabled(False)
        line_edit.setReadOnly(False)
        line_edit.setObjectName(name)
        return line_edit
    