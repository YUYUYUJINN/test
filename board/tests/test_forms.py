from django.test import TestCase
from board.forms import PostForm


class TestForms(TestCase):
    def test_post_form_valid_data(self):
        postForm = PostForm(data={'title': 'title1', 'contents': 'contents1'})
        self.assertTrue(postForm.is_valid())

    def test_post_form_invalid_no_title(self):
        postForm = PostForm(data={'contents': 'contents1'})

        self.assertFalse(postForm.is_valid())
        self.assertEqual(len(postForm.is_valid()), 1)

    def test_post_form_invalid_no_contents(self):
        postForm = PostForm(data={'title': 'title1'})

        self.assertFalse(postForm.is_valid())
        self.assertEqual(len(postForm.is_valid()), 1)

    def test_post_form_valid_no_data(self):
        postForm = PostForm(data={})

        self.assertFalse(postForm.is_valid())
        self.assertEqual(len(postForm.is_valid()), 2)
