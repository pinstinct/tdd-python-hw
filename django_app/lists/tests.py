from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from .models import Item
from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_reslove_to_home_page_view(self):
        # resolve는 장고 내부 함수로, URL을 해석해 일치하는 뷰 함수를 찾는다.
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     self.assertTrue(response.content.startswith(b'<html>'))
    #     self.assertIn(b'<title>To-Do lists</title>', response.content)
    #     self.assertTrue(response.content.strip().endswith(b'</html>'))

    # 리팩토링을 통해 뷰와 템플릿을 분리하면 위와 같은 방법으로 테스트코드를 작성할 필요가 없다.
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('lists/home.html')
        # .decode를 이용해 response.content 바이트 데이터를 파이썬 유니코드 문자열로 변환
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        # 테스트 설정을 위한 코드
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        # 실제 함수 호출
        response = home_page(request)

        # Assertion 코드
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '신규 작업 아이템')

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        # 더 이상 request.content가 템플릿에 렌더링되지 않으므로 assertion을 제거
        # response이 HTTP 리디렉션을 하기 때문에 상태코드가 302가 되며,
        # 브라우저는 새로운 위치를 가리킨다.
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(second_saved_item.text, '두 번째 아이템')


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        # 뷰 함수를 바로 호출하지 않고,
        # 장고의 TestCase 속성인 self.client를 사용한다.
        # 여기에 테스트할 URL을 .get한다.
        response = self.client.get('/lists/the-only-list-in-the-world/')

        # assertIn(response.content.decode())를 사용하지 않고,
        # 장고가 제공하는 assertContains 메서드를 사용한다.
        # 이 메소드는 응답 내용을 어떻게 처리해야 하는지 안다.
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
