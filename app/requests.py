from newsapi import NewsApiClient
# from ..config import
class NewsRequests:
    API_KEY = 'b6b97041f75646a49484f3adc0ff7156'
    n = NewsApiClient(api_key=API_KEY)
    def get_top_headlines(self,**kwargs):
        return self.n.get_top_headlines(**kwargs)
    def get_everything(self,**kwargs):
        return self.n.get_everything(**kwargs)
    def get_sources(self,**kwargs):
        return self.n.get_sources(**kwargs)