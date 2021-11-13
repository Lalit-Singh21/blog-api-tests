from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        #or
        self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')
        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        b.posts.append('test1')
        self.assertEqual(b.__repr__(), 'Test by Test Author (2 posts)')

        b2 = Blog('Test Another', 'Another Test Author')
        self.assertEqual(b2.__repr__(), 'Test Another by Another Test Author (0 posts)')
        b2.posts = ['test1', 'test2', 'test3']
        self.assertEqual(b2.__repr__(), 'Test Another by Another Test Author (3 posts)')
        #should be in integration test as it tests creating post object from different package
        b2.create_post("1234", "asdf")
        self.assertEqual(b2.__repr__(), 'Test Another by Another Test Author (4 posts)')







