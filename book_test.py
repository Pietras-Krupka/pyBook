import unittest

from book import Book


class testBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('Wiedźmin', 'Sapkowski', 2000)
    def test_get_info(self):
        text_correct = 'Książka: Wiedźmin Autor: Sapkowski Rok: 2000'
        text_result = self.book.get_info()
        self.assertEqual(text_correct, text_result)
if __name__ == '__main__':
    unittest.main()
    def change_title(self, new_title):
        self.title = new_title
    def change_author(self, new_author):
        self.author = new_author
    def change_year(self, new_year):
        self.year = new_year