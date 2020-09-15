import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('https://image.tmdb.org/t/p/w500/khsjha27hbs','Kingkrusha','Python Must Be Crazy','A thrilling new Python Series',129993,'Read more')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()