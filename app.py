import sys
from tests.Unit.blog_test import BlogTest
from blog import Blog

MENU_PROMPT = "Enter c to create a blog,\n " \
              "l to list blogs,\n " \
              "r to read one,\n " \
              "p to create a post\n" \
              " or q to quit: "
POST_TEMPLATE = '''
--{}--
{}'''
blogs = dict() # blog name: blog object

def ask_createblog():
    #ask the user to title and author to create a blog
    # store it the blogs dictionary
    # args = dict(title=input("Enter Title: "),
    #             author=input("Enter Author: "))
    # for k, v in args.items():
    #     title = k
    #     author = v
    #     break
    # blogs[k.strip()] = Blog(**args)
    title = input("Enter title: ")
    author = input("Enter author: ")
    #adding in blogs dictionary blog title: blog object
    blogs[title] = Blog(title, author)
    # print(f"Creating Blog: {blogs[title]}")

def ask_read_blogs():
    # ask for a blog title, and print the posts in blog
    # get blog object by title from blogs dict
    title = input("Enter the title you want to read: ")
    print_posts(blogs[title])

def print_posts(blog):
    #print post from blogs.posts list having post objects
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    # ask for blog title and post content and create new post
    blog_name = input("Enter a blog title you want to write post in: ")
    title = input("Enter your post title: ")
    content = input("Enter your post content: ")
    #blogs dict is initialised with blog title and blog abject
    # from the test ask_create_post
    blogs[blog_name].create_post(title, content)

def quit():
    sys.exit(0)


def menu():
    #show the user available blogs
    #let the user make a choice
    #Do something with choice
    #Exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_createblog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blogs()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def menu_old():
    #show the user available blogs
    #let the user make a choice
    #Do something with choice
    #Exit
    print_blogs()
    menu_dict = {
        'c': ask_createblog,
        'l': print_blogs,
        'r': ask_read_blogs,
        'p': ask_create_post,
        'q': quit,
    }
    get_selection = True
    while get_selection:
        selection = input(MENU_PROMPT)
        action = menu_dict.get(selection) #calling the function

        if action:
            action()
            # print(f"action::{action}")  # prints function reference
            get_selection = False
        else:
            print(f"{selection} is not a valid selection")
            continue

def print_blogs():
    #print available blogs
    for key, blog in blogs.items(): #[(blogname, blog),(blogname, blog)..]
        print('- {}'.format(blog))


if __name__ == "__main__":
    pass