import builtins
from unittest import TestCase
from unittest.mock import patch # for patching
import app
from app import menu
from blog import Blog

class AppTest(TestCase):

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_createblog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
                app.menu()
                mocked_ask_create_blog.assert_called()

    def test_menu_calls_createBlog_blog_is_not_none(self):
        blog = Blog('Test Create Blog', 'Test Author')
        app.blogs = {'Test Create Blog': blog}
        with patch('builtins.input') as mocked_input:
            #the blog is no longer created once we mock it so need to call blog = Blog('','')..and app.blogs = {'':blog}
            with patch('app.ask_createblog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
                app.menu()
                self.assertIsNotNone(app.blogs.get('Test Create Blog'))
                mocked_ask_create_blog.assert_called()

    def test_selection(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('l', 'q')
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blog(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('l', 'q')
                app.menu()
                mocked_print_blogs.assert_called()


    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')


    def test_Ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ("Test", "Test Author")
            app.ask_createblog()
            # value of blog object from blogs dict (having key = Test1), which is returned by __repr__ method of Blog class
            self.assertIsNotNone(app.blogs.get('Test'))
            self.assertEqual("Test by Test Author (0 posts)".lower().strip(), str(app.blogs.get('Test')).lower().strip())

    def test_ask_read_blog(self):
        #test print_posts function was called from ask_read_blog
        # with parameter blog object
        blog = Blog("Test", "Test Author")
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print:
                app.ask_read_blogs()
                mocked_print.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog("Test", "Test Author")
        blog.create_post("Test", "Test Content")
        #optional as we are not testing blogs dict
        #app.blogs = {'Test': blog}
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            #blog.posts[0] is the first element of post object in Blog class
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post_content(self):
        #post = Post("Post title", "Post content")
        #or as below
        blog = Blog("Test", "Test Author")
        blog.create_post("Post title", "Post content")
        expected_print = '''
--Post title--
Post content'''
        with patch('builtins.print') as mocked_print:
            # app.print_post(post) # if using post = Post() method in first line
            app.print_post(blog.posts[0])
            mocked_print.assert_called_with(expected_print)

    def ask_create_post(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect('Test', 'Test Title', 'Test Content')
            app.ask_create_post()
            self.assertEqual(blog.posts[0].title, 'Test Title')
            self.assertEqual(blog.posts[0].content, 'Test Content')
