from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    # dict.get(key, default=None)
    # key : dict에서 key를 검색
    # default : key가 없을 경우, default를 반환
    return render(request, 'lists/home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
