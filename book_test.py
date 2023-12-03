import unittest

from book import Book


class testBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('Wiedźmin', 'Sapkowski', 2000)
    def test_get_info(self):
        text_correct = 'Książka: Wiedźmin Autor: Sapkowski Rok: 2000'
        text_result = self.book.get_info()
        self.assertEqual(text_correct, text_result)
    def test_change_title(self):
        self.book.change_title('Miecz przeznaczenia')
        self.assertEqual('Miecz przeznaczenia', self.book.title)
    def test_change_author(self):
        self.book.change_author('Andrzej Sapkowski')
        self.assertEqual('Andrzej Sapkowski', self.book.author)
    def test_change_year(self):
        self.book.change_year(2000)
        self.assertEqual(2000, self.book.year)

if __name__ == '__main__':
    unittest.main()
