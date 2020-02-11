#뷰 작성용 임포트
import json

from .models import SearchList
from django.views import View

from django.http import HttpResponse, JsonResponse

# 크롤링용 임포트
import requests

from bs4 import BeautifulSoup

# 뷰 작성 시작
class SearchListView(View):
    def post(self, request):
        SearchList.objects.all().delete()
        data = json.loads(request.body)


        # HTTP GET Request
        req = requests.get(
            f'https://search.naver.com/search.naver?where=post&sm=stb_jum&query={data["query"]}')
        
        # HTML 소스 가져오기
        html = req.text

        ## html을 python 객체로 파싱
        soup = BeautifulSoup(html,'html.parser')

        post_title = soup.select(
            'dl > dt > a.sh_blog_title._sp_each_url._sp_each_title'
        )

        posting_date = soup.select(
        'dl > dd.txt_inline'
        )

        blog_url = soup.select(
            'dl > dd.txt_block > span > a.url'
            
        )

        for item in zip(post_title, posting_date, blog_url):
            SearchList(
                post_title=item[0].text,
                posting_date=item[1].text,
                blog_url=item[2].text,
            ).save()
        
        return HttpResponse(status=200)

    def get(self, request):
        return JsonResponse({'search list : ' : list(SearchList.objects.values())}, status=200)

