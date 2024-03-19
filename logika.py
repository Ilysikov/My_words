import random
import random
from typing import List, Union

from SQL_tab import my_tabs
from class_Text import Text


# передает пользовательский ввод для последующей обработки классу Trans_ter
class Input_new_word:
    def __init__(self, name: str, class_obj: object) -> None:
        # name - ключ словаря для последующей записи значения
        self.name_object_ = name
        # экземпляр класса Trans_ter хранящий соответствующий словарь 
        self.n_ap = class_obj

    def new_w(self, txt: str) -> None:
        # txt - введеный пользователем текст
        self.w = txt
        # сохранение текста в виде значения ранее созданного словаря
        self.n_ap.new_w_ap(w_ap=self.w, name=self.name_object_)
        return self.w, self.name_object_


# передает пользовательский ввод для последующей обработки классу Tran_tren(Trans_ter)
class Input_trenirovka(Input_new_word):
    def new_w(self, txt: str) -> None:
        self.w = txt
        self.n_ap.new_w_ap(w_ap=self.w, name=self.name_object_)
        return self.w


# дочерний класс для обработки ввода пользователем транскрипции слова
class Transcrition(Input_new_word):

    def new_w(self, txt: str) -> None:
        # проверяет введена ли транскрипция со скобками
        if len(txt.strip()) > 2 and txt[0] == '[':
            self.tran = txt
        elif txt.strip():
            self.tran = f"[{txt.strip()}]"
        else:
            self.tran = ''
        self.n_ap.new_w_ap(w_ap=self.tran, name=self.name_object_)
        return self.tran


# при создании экземпляра создает словарь с пустыми значениями
# пользовательский ввод добавляется, как значение в словарь
# данный класс содержит методы запускающие поиск по словарю и отображение слова
class Trans_ter:
    def __init__(self, dict_word: dict = {'self.e': '', "self.r": '',
                                          "self.t": '', "self.tran": ''}) -> None:
        self.dict_word = dict_word
        self.trenirovka = See_word()

    def new_w_ap(self, w_ap: str, name: str) -> None:
        self.dict_word[name] = w_ap

    def comand_serch(self) -> None:
        word = W_search()
        word.count_tab()
        word.search_(self.dict_word)

    def comand_see(self) -> None:
        self.trenirovka.count_tab()
        self.trenirovka.tran_column()
        self.trenirovka.play()


# дочерний класс обрабатывает пользовательский ввод в процессе тренировки
class Tran_tren(Trans_ter):
    def chek_create(self) -> None:
        go = Chek(dict_word=self.dict_word, trenirovka=self.trenirovka)
        go.check_word()


# содержит множество класс-методов необходимые для возврата новых значений,
# которые присваиваются виджетам
class slc:
    @classmethod
    def po(cls, pole_1: object, pole_2: object, pole_3: object,
           pole_4: object, pole_5: object, pole_6: object,
           pole_7: object, pole_8: object,
           pole_9: object, pole_10: object, model: object) -> None:
        cls.label_NT_str_01 = pole_1
        cls.label_NT_str_02 = pole_2
        cls.label_T_str_05 = pole_3
        cls.pushButton_T_skip = pole_4
        cls.lineEdit_T_input_field = pole_5
        cls.label_T_word = pole_6
        cls.label_T_str_04 = pole_7
        cls.label_T_str_01 = pole_8
        cls.label_T_str_03 = pole_9
        cls.progress = pole_10
        cls.model = model

    @classmethod
    def tran_04(cls, str_04: str) -> None:
        cls.label_T_str_04.setText(str_04)

    @classmethod
    def sel(cls) -> None:
        cls.model.select()

    @classmethod
    def play_tran(cls, str_skip: str, str_T_input: str) -> None:
        cls.pushButton_T_skip.setText(str_skip)
        cls.lineEdit_T_input_field.clear()
        cls.lineEdit_T_input_field.setPlaceholderText(str_T_input)

    @classmethod
    def t_word(cls, str_T_word: str) -> None:
        cls.label_T_word.setText(str_T_word)

    @classmethod
    def lab(cls, str_01: str, str_02: str, str_05: str) -> None:
        cls.label_NT_str_01.setText(str_01)
        cls.label_NT_str_02.setText(str_02)
        cls.label_T_str_05.setText(str_05)

    @classmethod
    def label_t_01(cls, t_01: str) -> None:
        cls.label_T_str_01.setText(t_01)
        return True

    @classmethod
    def label_t_03(cls, t_03: str, prog_int: float) -> None:
        cls.label_T_str_03.setText(t_03)
        cls.progress.setValue(int(prog_int))

    @classmethod
    def ret1(cls, list_: list) -> None:
        cls.list_ = list_

    @classmethod
    def ret1__(cls) -> list:
        return cls.list_

    @classmethod
    def percent_(cls, percent: float) -> None:
        cls.percent = percent

    @classmethod
    def percent_ret(cls) -> float:
        return cls.percent

    @classmethod
    def column_(cls, column: str) -> None:
        cls.column = column

    @classmethod
    def column_ret(cls) -> str:
        return cls.column

    @classmethod
    def column_chek_(cls, column_chek: str) -> None:
        cls.column_chek = column_chek

    @classmethod
    def column_chek_ret(cls) -> str:
        return cls.column_chek

    @classmethod
    def columnask_(cls, columnask: str) -> None:
        cls.columnask = columnask

    @classmethod
    def columnask_ret(cls) -> str:
        return cls.columnask

    @classmethod
    def question_(cls, question: str) -> None:
        cls.question = question
        return

    @classmethod
    def question_ret(cls) -> str:
        return cls.question

    @classmethod
    def number_(cls, number: int) -> None:
        cls.number = number

    @classmethod
    def number_ret(cls) -> int:
        return cls.number


# класс отвечающий за поиск слова в таблице "word_"
class W_search:
    # запускается только из основного кода, создает базу данных
    def create_sql(self):
        self.data=my_tabs()
        self.data.connect_()
        self.data.create_file_data()
        self.data.open_data()
        self.data.cursor_()
        self.data.one_tab()
        self.data.two_tab()
        self.close_tran(data=self.data)

    def create_sql_2(self):
        self.data2 = my_tabs()

        # self.data.open_data()
        self.data2.cursor_()


    def open_connect(self):
        self.data = my_tabs()
        self.data.open_data()
        self.data.cursor_()
    # возвращает количество слов
    def count_tab(self, pole='english', tab='words_') -> int:
        if tab=='progress_':
            pole='answer'
        v = my_tabs()
        v.cursor_()
        v.select_(search_=f"COUNT({pole})", tab_=tab)
        self.count_table = v.fetchone_
        return self.count_table

    # возвращает объект в котором сохранены данные из таблицы
    def my_select(self) -> object:
        self.s_object = my_tabs()
        self.s_object.cursor_()
        self.s_object.select_(search_="english, russian, translit, transkrip",
                  tab_="words_")
        return self.s_object

    # возвращает список слов сохраненных в определенной строке и определенном столбце
    def my_list(self, my_object: object, column: str) -> list:
        list_ = my_object.value_column(column).lower().split(',')
        list2 = [w.strip() for w in list_]
        return list2

    # поиск слова в таблице
    def search_(self, dict_word: dict) -> None:
        self.dict_word = dict_word
        self.text_ = Text()
        n_wor = New_word()
        w = self.my_select()
        if self.count_table > 0:
            # проверка отсутствия слова в каждой строке
            for index in range(self.count_table):
                w.seek_(index)
                if w.value_column('english') == self.dict_word['self.e']:
                    if w.value_column('russian') == self.dict_word['self.r']:
                        slc.lab(str_01=self.text_.c_text(key_='nt_1_02'),
                                str_02=self.text_.i_text(key_='nt_2_02', list_dic={'index': str(index + 1)}),
                                str_05=self.text_.i_text(key_='t_05', list_dic={'self.count_table': self.count_table}))
                        break
                    elif w.value_column('russian') != self.dict_word['self.r']:
                        self.list2 = self.my_list(my_object=w, column='russian')
                        if self.dict_word['self.r'] in self.list2:
                            slc.lab(str_01=self.text_.c_text(key_='nt_1_02'),
                                str_02=self.text_.i_text(key_='nt_2_02',list_dic={'index':str(index+1)}),
                                str_05=self.text_.i_text(key_='t_05', list_dic={'self.count_table':self.count_table}))
                            break
                        elif self.dict_word['self.r'] not in self.list2:
                            continue
                elif w.value_column('english') != self.dict_word['self.e'] and index != self.count_table - 1:
                    continue
                elif w.value_column('english') != self.dict_word['self.e'] and index == self.count_table - 1:
                    n_wor.app_word(self.dict_word)
                    n_wor.new_word_()
                    n_wor.new_word_continue()
        else:
            n_wor.app_word(self.dict_word)
            n_wor.new_word_()
            n_wor.new_word_continue()
# добавление нового слова
    @classmethod
    def close_tran(cls, data):
        cls.data=data
    @classmethod
    def close(cls):
        cls.data.cursor_close()
    def delete_d(self, dict_delete:dict):
        v = my_tabs()
        v.cursor_()
        v.delete_data(name_tab=dict_delete['name_tab'], delete_data=dict_delete['delete_data'])
        return self.count_tab(tab=dict_delete['name_tab'])
class New_word:
    # принимает и возвращает в виде списка значения словаря
    def app_word(self, dict_word: dict) -> list:
        self.list_word = [dict_word[i] for i in dict_word.keys()]
        return self.list_word
    # добавление нового слова
    def new_word_(self) -> None:
        h = my_tabs()
        h.cursor_()
        h.insert_(tab_="words_", list_tab=["english", "russian", "translit", "transkrip"],
                  list_=self.list_word)
        h.select_(search_="COUNT(english)", tab_="words_")
        loc_r = See_word()
        s=loc_r.my_select2(number=loc_r.count_tab()-1)
        ask = loc_r.my_list(my_object=s, column="russian")

        return ask
    def new_word_continue(self):
        slc.sel()  # изменение таблица во вкладке "Редактирование"
        self.text_ = Text()
        count = W_search.count_tab(self)
        list_cancel = slc.ret1__()
        # очистка полей ввода
        nw_can = Canc(list_cancel)
        nw_can.cancel_()
        # изменение текста
        slc.lab(str_01=self.text_.i_text(key_='nt_1_03',
                                         list_dic={'english': self.list_word[0],
                                                   'russian': self.list_word[1]}),
                                                    str_02=self.text_.c_text(key_='nt_1'),
                                                    str_05=self.text_.i_text(key_='t_05',
                                                    list_dic={'self.count_table': count}))

# отображение рандомным образом слов словаря, их сохранения и передача для последующей обработки
class See_word(W_search):
    # значения - переводимый язык
    def tran_column(self) -> None:
        self.column = slc.column_ret()
        self.column_chek = slc.column_chek_ret()
        return self.column

    # переопределение родительского метода
    # добавляем поиск и сохранение в экземпляр строки, найденной по номеру
    def my_select2(self, number: int) -> object:
        super().my_select().seek_(number)
        return self.s_object
    # процесс тренировки
    def play(self) -> None:
        self.text = Text()
        # необходима при перезапуске
        slc.play_tran(str_skip=self.text.c_text(key_='t_skip_2'),
                      str_T_input=self.text.c_text(key_='input'))
        if self.count_table > 0:
            # по рандомну избранному номеру строки возвращается слово на языке, который задал пользователь
            self.number = random.randint(0, self.count_table - 1)
            slc.number_(self.number)
            s = self.my_select2(number=self.number)
            self.list2 = self.my_list(my_object=s, column=self.column)
            self.question = self.list2[random.randint(0, len(self.list2) - 1)]
            slc.question_(self.question)
            slc.t_word(str_T_word=self.question)
            if self.column == 'english':
                self.english_trans = self.question
                fonet = Fonetika()
                fonet.trans_eng(number=self.number, english_trans=self.english_trans)
        else:
            slc.t_word(str_T_word=self.text.c_text(key_='T_word_0'))


# проверка пользовательского ввода при тренировке
class Chek(See_word):
    def __init__(self, dict_word: dict, trenirovka: object) -> None:
        super().__init__()
        self.dict_word = dict_word
        self.trenirovka = trenirovka
        self.text = Text()

    def check_word(self) -> None:
        self.trenirovka.play()
        slc.label_t_01(t_01=self.text.c_text(key_='t_1_3'))
        fon = Fonetika()
        self.column = slc.column_ret()
        self.column_chek = slc.column_chek_ret()
        self.question = slc.question_ret()
        self.percent = slc.percent_ret()
        self.number = slc.number_ret()
        fon.trans_eng(number=self.number, english_trans=self.question)
        answer = self.dict_word['trenirovka']
        if self.question and answer:
            x = self.my_select2(number=self.number)
            self.list2 = self.my_list(my_object=x, column=self.column_chek)
            if answer in self.list2:
                slc.label_t_01(t_01=self.text.i_text(key_='t_1_2',
                                                     list_dic={'self.question': self.question,
                                                               'self.w': answer}))
                self.answer_0 = answer
                if self.column_chek == 'english':
                    self.english_trans = self.answer_0
                    fon.trans_eng(self.number, self.english_trans)
                pro = Search_prog()
                pro.search_(self.answer_0, self.question, self.percent)
                pro.search_word()
                self.trenirovka.play()
            elif answer not in self.list2:
                slc.label_t_01(t_01=self.text.c_text(key_='t_1_3'))
        else:
            slc.label_t_01(t_01=self.text.c_text(key_='t_1_4'))
        return answer

# класс отвечающий за поиск и отображение транскрипции или/транслитерации слова
class Fonetika:
    # поиск и сохранение в переменные транскрипции и транслитерации соответствующего слова
    def trans_eng(self, number: int, english_trans: str) -> None:
        t = my_tabs()
        self.text = Text()
        t.cursor_()
        t.select_(search_="english,russian,translit,transkrip", tab_="words_")
        t.seek_(number)
        self.translit = t.value_column('translit')
        self.transkrip = t.value_column('transkrip')
        # присвоение новых значений и вызов соответствующего класс-метод scl
        if not self.translit.strip() and not self.transkrip.strip():
            str_04 = self.text.c_text(key_='t_04')
        elif not self.translit.strip() and self.transkrip.strip():
            str_04 = self.text.i_text(key_='t_04_2', list_dic={'english_trans': english_trans,
                                                               'self.transkrip': self.transkrip})
        elif self.translit.strip() and not self.transkrip.strip():
            str_04 = self.text.i_text(key_='t_04_3', list_dic={'english_trans': english_trans,
                                                               'self.translit': self.translit})
        elif self.translit.strip() and self.transkrip.strip():
            str_04=self.text.i_text(key_='t_04_4',list_dic={'english_trans':english_trans,
                                                            'self.transkrip':self.transkrip,
                                                            'self.translit':self.translit})
        slc.tran_04(str_04)
        return True


class Search_prog:
    # поиск слова в таблице "progress_"
    def search_(self, answer: str, question: str, percent: float) -> List[Union[str, float]]:
        self.answer_0 = answer
        self.question = question
        self.percent = percent
        return [self.answer_0, self.question, self.percent]

    def search_word(self):
        c = my_tabs()
        c.cursor_()
        c.select_(search_="COUNT(answer)", tab_="progress_")
        self.count_table_two = c.fetchone_
        if self.count_table_two > 0:
            c.select_(search_="answer, question, percent", tab_="progress_")
            for index in range(self.count_table_two):
                c.seek_(index)
                if c.value_column('answer') == self.answer_0:
                    if c.value_column('question') == self.question:
                        break
                    elif c.value_column('question') != self.question:
                        self.add_two_table()
                        self.progress_()
                        break
                elif c.value_column('answer') != self.answer_0 and index != self.count_table_two - 1:
                    continue
                elif c.value_column('answer') != self.answer_0 and index == self.count_table_two - 1:
                    self.add_two_table()
                    self.progress_()
        elif self.count_table_two == 0:
            self.add_two_table()
            self.progress_()


    # добавление слова в случае его отсутствия
    def add_two_table(self) -> int:
        q = my_tabs()
        q.cursor_()
        q.insert_(tab_="progress_", list_tab=["answer", "question", "percent"],
                  list_=[self.answer_0, self.question, self.percent])
        q.select_(search_="COUNT(answer)", tab_="progress_")
        count_two_tab=q.fetchone_
        return count_two_tab
        # перасчет суммы значений таблицы определяющая уровень прогресса

    def progress_(self) -> None:
        v = my_tabs()
        v.cursor_()
        v.select_(search_="SUM(percent)", tab_="progress_")
        num_ = v.fetchone_
        if not num_:
            self.num = 0
        else:
            self.num = num_
        self.list_03 = []
        level_dic = {800: "A1 (Elementary)", 2000: "А2 (Pre-intermediate)", 3500: "B1 (Intermediate)",
                     6000: "B2 (Upper-Intermediate)", 10000: "C1 (Advanced)", 16000: "C2 (Proficient)"}
        for c, key in enumerate(level_dic):
            self.list_03.append(key)
            if key >= self.num and c > 0:
                self.level_minus = self.list_03[c - 1]
                self.level_int = key
                self.level = level_dic[key]
                break
            elif key >= self.num and c == 0:
                self.level_minus = 0
                self.level_int = key
                self.level = level_dic[key]
                break
            elif key == 16000 and self.num > key:
                self.level_int = 16000
                self.level = level_dic[key]
        if self.num == None:
            self.sum_percent = 0
        elif self.num == 0:
            self.sum_percent = 0
        else:
            self.sum_percent = 100 / ((self.level_int - self.level_minus) / (self.num - self.level_minus))
            slc.label_t_03(t_03=str(round(self.sum_percent, 2)) + "% " + self.level, prog_int=self.sum_percent)

class Chang(object):
    # переопределение значений в списке, 
    # которые соответствуют переменным в классе Ui_MainWindow
    def colu_n(self, list: list) -> list:
        self.text_ = Text()
        list[3].setText(self.text_.c_text(key_="t_skip"))
        list[4].clear()
        list[5].clear()
        list[5].setPlaceholderText(self.text_.c_text(key_="input"))
        list[6].setText(self.text_.c_text(key_="t_1"))
        if list[0] == self.text_.c_text(key_='rus'):
            list[1].setText(self.text_.c_text(key_="t_rus"))
            list[2].setText(self.text_.c_text(key_="t_eng"))
            list[7] = self.text_.c_text(key_="t_eng")
            list[0] = self.text_.c_text(key_='eng')
            list[9] = self.text_.c_text(key_='rus')
            list[10] = self.text_.c_text(key_='e_percent')
        elif list[0] == self.text_.c_text(key_='eng'):
            list[1].setText(self.text_.c_text(key_="t_eng"))
            list[2].setText(self.text_.c_text(key_="t_rus"))
            list[7] = self.text_.c_text(key_="R_rus")
            list[0] = self.text_.c_text(key_='rus')
            list[9] = self.text_.c_text(key_='eng')
            list[10] = self.text_.c_text(key_='r_percent')
        list[8].setText(list[7])
        return [list[0], list[7], list[9], list[10]]


# перемещение курсора
class Focus_tran:
    def __init__(self, pole: object) -> None:
        self.pole = pole

    def foc_(self) -> None:
        self.pole.setFocus()


# очистка полей ввода
class Canc:
    def __init__(self, list_: list) -> None:
        self.list_ = list_
        self.text_ = Text()

    def cancel_(self) -> None:
        for i in self.list_:
            i.clear()
            i.setPlaceholderText(self.text_.c_text(key_='input'))
        self.list_[0].setFocus()
