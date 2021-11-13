class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        return dict(
            title=self.title,
            content=self.content)
        # return {
        #     'title':self.title,
        #     'content':self.content,
        # }
