import unittest

from app.models import Comment,User,Blog
from app import db

class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.user_Leah = User(username = 'Leah',password = '1234', email = 'leahgakii74@gmail.com')
        self.new_blog = Blog(title="my country code"blog='super cool',user = self.user_Leah )

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title,'my country code ')

        self.assertEquals(self.new_blog.blog,'super cool')
        self.assertEquals(self.new_blog.user,self.user_Leah)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)
