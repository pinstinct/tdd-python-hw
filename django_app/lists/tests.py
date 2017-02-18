from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_reslove_to_home_page_view(self):
        # resolve는 장고 내부 함수로, URL을 해석해 일치하는 뷰 함수를 찾는다.
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('lists/home.html')
        # .decode를 이용해 response.content 바이트 데이터를 파이썬 유니코드 문자열로 변환
        self.assertEqual(response.content.decode(), expected_html)
