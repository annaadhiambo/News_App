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

    def test_name(self):
        name_var = self.new_news.name
        self.assertTrue(name_var == "Kingkrusha")

    def test_title(self):
        title_var = self.new_news.title
        self.assertTrue(title_var == "Python Must Be Crazy")

    def test_description(self):
        description_var = self.new_news.description
        self.assertTrue(description_var == "A thrilling new Python Series")

    def test_publishedAt(self):
        publishedAt_var = self.new_news.publishedAt
        self.assertTrue(publishedAt_var == 129993)

    def test_url(self):
        url_var = self.new_news.url
        self.assertTrue(url_var == "Read more")
        # try:
        #     self.assertTrue(name_var == "anna")
        # except:
        #     pass
            



if __name__ == '__main__':
    unittest.main()