from unittest import TestCase, main
from logika import New_word
class app_word_tests(TestCase):
    def test_list_equal(self):
        self.assertEqual(New_word.app_word(self,dict_word={'english':'five','russian':'пять',"transcription":'','transliteration':''}),
                         ['five','пять', '', ''])
        self.assertEqual(New_word.app_word(self, dict_word={'english': 'five', 'russian': 'пять', "transcription": None,
                                                            'transliteration': None}),
                         ['five', 'пять', None, None])
    def test_raise(self):
        with self.assertRaises(AttributeError):
            self.assertEqual(New_word.app_word(self,
                                               dict_word=90))

            self.assertEqual(New_word.app_word(self,
                                               dict_word={}))
            self.assertEqual(New_word.app_word(self,
                                               dict_word={'o'}))





if __name__ == '__main__':
    main()