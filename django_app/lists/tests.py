from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_reslove_to_home_page_view(self):
        # resolve는 장고 내부 함수로, URL을 해석해 일치하는 뷰 함수를 찾는다.
        found = resolve('/')
        self.assertEqual(found.func, home_page)
