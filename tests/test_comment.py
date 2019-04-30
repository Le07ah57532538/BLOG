import unittest

from app.models import Comment,User
from app import db

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.user_Leah = User(username = 'Leah',password = '1234', email = 'leahgakii74@gmail.com')
        self.new_comment = Comment(comment='cool',user = self.user_Leah )

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):

        self.assertEquals(self.new_comment.comment,'cool')
        self.assertEquals(self.new_comment.user,self.user_Leah)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
