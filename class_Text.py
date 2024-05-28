class Text(object):
    # словарь данного метода содержит статичные значения, 
    # которые не нужно переопределять  
    def c_text(self, key_: str)-> str or int:
        text_dic={
            'None':'',
            'rus':'russian',
            'eng':'english',
            't_lit':'translit',
            't_rip':'transkrip',
            'R_rus':'Русский',
            'r_percent':0.7,
            'e_percent':0.3,
            'input':'Введите текст',
            'save':"Добавить в словарь",
            'w_english':"Слово на Английском",
            'w_russian':"Перевод на Русский",
            'w_translit':"Транслитиреция на русском языке (необязательно)",
            'w_transkrip':"Транскрипция слова (необязательно)",
            'cancel':"Отмена",
            'nt_1':"Введите слово на Английском языке и его перевод на Русский язык.",
            'nt_2':"Также вы можете сохранить транслитерацию и/или транскрипцию слова.",
            'tab_widget_nt':"Добавить новое слово",
            't_chek':"Проверить",
            "t_skip":"Тренироваться",
            't_skip_2':"Пропустить",
            "t_rus":"  Русский   ",
            't_eng':"Английский",
            'slider_':"<=>",
            't_1':"Ваш перевод:",
            't_2':"Ваш прогресс:",
            'tab_widget_t':"Тренировка",
            "tab_widget_r":"Редактирование",
            'T_word_0':'Извините, но в Вашем словаре еще нет слов.',
            't_1_3':"Простите, вы дали неверный ответ. Попробуйте еще раз!",
            't_1_4':"Пока нечего проверять",
            't_04':"Увы, вы не добавили к этому слову его транскрипцию или транслитерацию",
            'nt_1_02':'Извините, но вы уже добавили это слово и его перевод в свой словарь'}
        return text_dic[key_]
    # значения словаря "self.dict_02" зависят от параметров данного метода
    def i_text(self, key_: str, list_dic: str)-> str:
        self.dict_b={
        "english":'',
        "russian":'',
        "self.count_table":'',
        "index":'',
        "self.transkrip":'',
        'english_trans':'',
        'self.translit':'',
        'self.question':'',
        'self.w':''}
        for i in list_dic.keys():
            self.dict_b[i]=list_dic[i]
        self.dict_02={
            'nt_1_03':f'''Слово "{self.dict_b['english']}"
            и его перевод "{self.dict_b['russian']}" добавлены в Ваш словарь.''',
            't_05':f"В Вашем словаре {self.dict_b['self.count_table']} слов.",
            'nt_2_02':f'''Вы их можете найти под номером {self.dict_b['index']}, во вкладке "Редактирование"''',
            't_04_2':f'''"{self.dict_b['english_trans']}" произносится: {self.dict_b['self.transkrip']}''',
            't_04_3':f'''"{self.dict_b['english_trans']}" произносится: "{self.dict_b['self.translit']}"''',
            't_04_4':f'''"{self.dict_b['english_trans']}" произносится: {self.dict_b['self.transkrip']} или русскими буквами – "{self.dict_b['self.translit']}"''',
            't_1_2':f'''Верно! Слово "{self.dict_b['self.question']}" переводится – "{self.dict_b['self.w']}"'''}
        return self.dict_02[key_]   
    def peremen_(self, col:str, label_T_str_00: object)->None:
        self.label_T_str_00=label_T_str_00
        self.columnask=col
    def ask_(self)->None:
        self.label_T_str_00.setText('Уже '+self.columnask)


