from django.test import TestCase
from django.urls import resolve
from board.views import create


class TestUrls(TestCase):
    def test_create_url_is_resolved(self):
        url = resolve('/board/create')  # url을 찾아서 해당하는 객체를 반환
        self.assertEqual(url.func, create)  # 본래 매핑시키려 했던 함수가 맞는지 검증