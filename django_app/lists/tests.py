from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from lists.views import home_page


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
        self.assertTrue(response.content.endswith(b'</html>'))
