from django.contrib.auth.models import User
from django.test import TestCase, Client
from board.models import Post


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user01', password='qwer1234')

    def test_post_create_GET_with_login(self):
        self.client.login(username='user01', password='qwer1234')
        response = self.client.get('/board/create')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/create.html')

    def test_post_create_GET_without_login(self):
        response = self.client.get('/board/create')
        self.assertEqual(response.status_code, 302)

    def test_post_create_POST_without_login(self):
        response = self.client.get('/board/create')
        # self.assertRedirects(response, '/accounts/login')
        self.assertEqual(response.url, '/accounts/login')
        self.assertEqual(response.status_code, 302)

    def test_post_create_POST_with_login(self):
        self.client.login(username='user01', password='qwer1234')
        response = self.client.post(
            '/board/create',
            data={'title': 'title1', 'contents': 'contents1'}
        )
        post = Post.objects.get(title='title1')
        self.assertEqual(post.title, 'title1')
        self.assertEqual(response.status_code, 302)

    def test_post_create_POST_with_check_title_length(self):
        self.client.login(username='user01', password='qwer1234')
        response = self.client.post(
            '/board/create',
            data={'title': 'a', 'contents': 'contents1'}
        )
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), '제목은 5글자 이상이어야 합니다.')
        self.assertEqual(response.status_code, 400)



