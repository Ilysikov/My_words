import sys
from unittest import TestCase, main, mock
from unittest.mock import patch, MagicMock
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from SQL_tab import my_tabs
from logika import (Input_new_word, Trans_ter, W_search, Transcrition, Tran_tren,
                    Input_trenirovka, New_word, Search_prog, Chek)
from Ui_MainWindow import Ui_MainWindow


class input_new_word_tests(TestCase):
    def new_word(self, name):
        self.ter = Trans_ter()
        new_ = Input_new_word(name=name, class_obj=self.ter)
        return new_

    def test_nv_eng(self):
        new = self.new_word(name='self.e')
        self.assertEqual(new.new_w(txt='cat'), ('cat', 'self.e'))
        self.assertEqual(new.new_w(txt='run'), ('run', 'self.e'))

    def test_nv_rus(self):
        new = self.new_word(name='self.r')
        self.assertEqual(new.new_w(txt='трус'), ('трус', 'self.r'))
        self.assertEqual(new.new_w(txt='почему?'), ('почему?', 'self.r'))

    def test_nv_t(self):
        new = self.new_word(name='self.t')
        self.assertEqual(new.new_w(txt='ран'), ('ран', 'self.t'))
        self.assertEqual(new.new_w(txt='гоу'), ('гоу', 'self.t'))


class Trancription_test(TestCase):
    def test_transkrip(self):
        self.ter = Trans_ter()
        new_ = Transcrition(name='self.tran', class_obj=self.ter)
        self.assertEqual(new_.new_w(txt='[dad]'), '[dad]')
        self.assertEqual(new_.new_w(txt='dad'), '[dad]')
        self.assertEqual(new_.new_w(txt=''), '')

class Input_trenirovka_test(TestCase):
    def test_trenirovka(self):
        self.clic_tren=Tran_tren(dict_word={'trenirovka':''})
        new_ = Input_trenirovka(name='trenirovka', class_obj=self.clic_tren)
        self.assertEqual(new_.new_w(txt='Try'), 'Try')
        self.assertEqual(new_.new_w(txt='dad'), 'dad')
        self.assertEqual(new_.new_w(txt=''), '')


class Sql_word_test(TestCase):
    def __init__(self, *args, **kwargs):
        super(Sql_word_test, self).__init__(*args, **kwargs)
        self.data_test: W_search=W_search()
        self.data_test.create_sql()
        self.exs = New_word()
        self.number=0

    # @patch('logika.New_word.app_word')
    def test_new_word_(self):


        self.exs.app_word(dict_word={'self.e': 'hohohojjj', "self.r": 'io',
                                        "self.t": 'den', "self.tran": '[k]'})

        self.assertEqual(self.exs.new_word_(),['io'])


        number:int=self.data_test.count_tab()
        number_two=number-1
        self.assertEqual(self.data_test.delete_d({'name_tab':'words_','delete_data':'"translit" = "den"'}),
                         number_two)

        # self.data_test.close()


class Sql_test_two(TestCase):
    def __init__(self, *args, **kwargs):
        super(Sql_test_two, self).__init__(*args, **kwargs)
        self.data_test = W_search()
        self.exs = New_word()
        self.prog=Search_prog()





    # @patch'logika.Search_prog.self.answer_0'
    def test_new_word_2(self):

        self.exs.app_word(dict_word={'self.e': 'hohohojjj', "self.r": 'Лес',
                                        "self.t": '', "self.tran": '[лдлдд]'})
        self.assertEqual(self.exs.new_word_(),['лес'])
        number: int = self.data_test.count_tab()
        number_two = number - 1
        self.assertEqual(self.data_test.delete_d({'name_tab': 'words_', 'delete_data': '"english" = "hohohojjj"'}),
                         number_two)
        # self.data_test.close()
    def test_new_word_3(self):

        self.exs.app_word(dict_word={'self.e': 'hohohojjj', "self.r": 'Бегемот',
                                        "self.t": '', "self.tran": '[лдлдд]'})
        self.assertEqual(self.exs.new_word_(),['бегемот'])
        number: int = self.data_test.count_tab()
        number_two = number - 1
        self.assertEqual(self.data_test.delete_d({'name_tab': 'words_', 'delete_data': '"transkrip" = "[лдлдд]"'}),
                             number_two)
    def new_word_4(self, word1='again_again', word2='снова_снова'):
        self.exs.app_word(dict_word={'self.e': word1, "self.r": word2,
                                        "self.t": '', "self.tran": '[лдлдд]'})
        self.assertEqual(self.exs.new_word_(),[word2])
        self.number: int = self.data_test.count_tab()
        return self.number-1

    def new_4_close(self, word1='"again_again"'):
        number_two = self.number - 1
        self.assertEqual(self.data_test.delete_d({'name_tab': 'words_', 'delete_data': f'"english" = {word1}'}),
                        number_two)



    def test_prog(self):
        self.prog.search_('hohohojjj', 'бегемот', 1.0)
        count_ = self.prog.add_two_table()
        count_two = count_ - 1
        if count_two==0:
            count_two=1
        self.assertEqual(self.data_test.delete_d({'name_tab': 'progress_', 'delete_data': '"answer" = "hohohojjj"'}),
                         count_two)


    def test_prog_2(self):
        self.prog.search_('hohohojjj', 'бегемот', 1.0)
        count_ = self.prog.add_two_table()
        count_two = count_ - 1
        if count_two==0:
            count_two=1
        self.assertEqual(self.data_test.delete_d({'name_tab': 'progress_', 'delete_data': '"answer" = "hohohojjj"'}),
                         count_two)
        # self.data_test.close()
    def test_prog_3(self):
        self.prog.search_('hohohojjj', 'бегемот', 1.0)
        count_ = self.prog.add_two_table()
        count_two = count_ - 1
        if count_two==0:
            count_two=1
        self.assertEqual(self.data_test.delete_d({'name_tab': 'progress_', 'delete_data': '"answer" = "hohohojjj"'}),
                         count_two)


class Check_test(TestCase):
    def __init__(self, *args, **kwargs):
        super(Check_test, self).__init__(*args, **kwargs)
        self.check_test=Chek(dict_word={'trenirovka':'again_again'}, trenirovka=mock.MagicMock())
        self.my = Sql_test_two()
    @patch('logika.Search_prog.search_word')
    @patch('logika.Search_prog.search_')
    @patch('logika.slc.label_t_01')
    @patch('logika.slc.column_ret')
    @patch('logika.slc.column_chek_ret')
    @patch('logika.slc.question_ret')
    @patch('logika.slc.percent_ret')
    @patch('logika.slc.number_ret')
    @patch('logika.Fonetika.trans_eng')
    def test_check(self, mock1, mock2, mock3, mock4, mock5, mock6,mock7, mock8, mock9):
        mock1.return_value=True
        mock2.return_value=self.my.new_word_4()
        mock3.return_value=0.7
        mock4.return_value='снова_снова'
        mock5.return_value='english'
        mock6.return_value='russian'
        mock7.return_value=True
        mock8.return_value=True
        mock9.return_value=True
        self.assertEqual(self.check_test.check_word(),'again_again')
        self.my.new_4_close()




    #
    # def test_mock(self, mock_trenirovka):
    #     mock.return_value = 'english'
    #     self.assertEqual(play(),number)





if __name__ == '__main__':
    main()
