class News:
    '''
    News class to define News object
    '''
    def __init__(self,urlToImage ,name, title,descripion,publishedAt, url):
        self.urlToImage = urlToImage
        self.name = name
        self.title = title
        self.descripion = descripion
        self.publishedAt = publishedAt
        self.url =url