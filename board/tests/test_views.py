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


    def test_post_create_GET_with_check_title_length(self):
        self.client.login(username='user01', password='qwer1234')
        response = self.client.post(
            '/board/create',
            date={'title': 'title1', 'contents': 'contents1'}
        )
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)  # 현재 에러 메세지가 하나만 담겨 있음
        self.assertEqual(str(messages[0]), '제목은 5글자 이상')  # 메세지에 들어있는 첫번째 메세지로 해당 멘트를 띄움
        self .assertEqual(response.status_code, 400)
