from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtSql import QSqlDatabase

class my_tabs(object):
    def connect(self)->None:
        self.con = QSqlDatabase.addDatabase("QSQLITE")
    def create_file_data(self,
                         name: str="/Users/ivanlysikov/PycharmProjects/pythonProject6/.venv/var/personal_dictionary.db")->None:
        self.con.setDatabaseName(name)
    def open_data(self)->None:
        self.con.open()
    def cursor_(self)->None:
        self.cursor=QSqlQuery()
    def one_tab(self,tab_n1: str="words_",language_1: str="english", 
                language_2: str="russian", 
                translit: str="translit", transkrip: str="transkrip")->None:    
        self.cursor.exec(f"""CREATE TABLE {tab_n1}
                    ({language_1} TEXT,
                    {language_2} TEXT,
                    {translit} TEXT,
                    {transkrip} TEXT)
                    """)
    def two_tab(self,tab_n2: str="progress_")->None:
        self.cursor.exec(f"""CREATE TABLE {tab_n2}
                (answer TEXT,
                question TEXT,
                percent TEXT)
                """)
    def select_(self, search_: str, tab_: str)->None:
        self.cursor.exec(f"SELECT {search_} FROM {tab_}")
    def seek_(self,index: int)-> bool:
        return self.cursor.seek(index)
    def value_column(self, column_: str)-> str:
        return self.cursor.value(column_)
    def insert_(self, tab_: str, list_tab: list, list_: list)->None:
        self.cursor.prepare(f'''INSERT INTO {tab_} ({",".join(list_tab)}) 
                            VALUES ({",".join(("? "*len(list_tab)).split())})
                            ''')
        for i in list_:
            self.cursor.addBindValue(i)
        self.cursor.exec()      
    def delete_(self, delete_data: str)->None:
        self.cursor.exec(f'DELETE FROM {delete_data}')
    def fetchone_(self)-> int:
        while (self.cursor.next()):
            self.count=self.cursor.value(0)
        return self.count
    def cursor_close(self):
        self.cursor.close()