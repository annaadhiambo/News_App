class News:
    '''
    News class to define News object
    '''
    def __init__(self,urlToImage ,name, title,description,publishedAt, url):
        self.urlToImage = urlToImage
        self.name = name
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.url =url