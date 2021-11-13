from post import Post


class Blog:
    def __init__(self, title='', author='', **kwargs):
        self.title = title
        self.author = author
        self.posts = []

    # will return string representation of Blog
    # repr method will represent the Blog method when we are debugging
    def __repr__(self):
        # print(f"<reprBlog>{self.title} by {self.author} ({len(self.posts)} post{'s' if len(self.posts) !=1 else ''})")
        return "{} by {} ({} post{})".format(self.title,
                                             self.author,
                                             len(self.posts),
                                             's' if len(self.posts) != 1 else '')

    def create_post(self, title, content):
        #create a post object and append it to posts list
        self.posts.append(Post(title, content))
        #print(f"createpost::::{self.posts[0].title}")
        #print([post.json() for post in self.posts])

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }

# b = Blog('tt','ta')
# print(b.json())
# b.create_post('testtitle', 'testcontent')
