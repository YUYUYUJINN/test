from django.contrib.auth.models import User
from django.test import TestCase, Client

from board.models import Post


class TestViews(TestCase):
    def setUp(self):  # 사용자 생성
        self.client = Client()
        self.user = User.objects.create_user(username='user01', password='qwer1234')

    def test_post_create_POST_with_login(self):
        self.client.login(username='user01', password='qwer1234')  # 로그인
        response = self.client.post(
            '/board/create',
            date={'title':'title1','contents':'contents1'}
        )
        post = Post.objects.get(title='title1')
        self.assertFalse(post.title, 'title1')
        self .assertEqual(response.status_code, 302)


    def test_post_create_GET_with_logout(self):
        response = self.client.get('/board/create')
        self .assertEqual(response.status_code, 302)  # 로그인 페이지로 리다이렉트 시킴
