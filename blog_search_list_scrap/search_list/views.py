# 뷰 작성용 임포트
import json

from .models import SearchList
from django.views import View

from django.http import HttpResponse, JsonResponse

# 크롤링용 임포트
import requests

from bs4 import BeautifulSoup

# csv 저장용 임포트
import csv

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
            ' dl > dt > a'
        )

        posting_date = soup.select(
        'dl > dd.txt_inline'
        )

        blog_url = soup.select(
            'dl > dd.txt_block > span > a.url'
            
        )


        with open('./csv/blog_lists.csv', mode='w') as blog_lists:
            blog_writer = csv.writer(blog_lists)
            blog_writer.writerow(["post_title", "posting_date","blog_url"])

            for list in zip(post_title, posting_date, blog_url):
                SearchList(
                    post_title=list[0].text,
                    posting_date=list[1].text,
                    blog_url=list[2].text,
                ).save()
                
                blog_writer.writerow([list[0].text, list[1].text, list[2].text])

        return HttpResponse(status=200)

    def get(self, request):
        result = []

        with open('./csv/blog_lists.csv', mode='r') as blog_lists:
            reader = csv.reader(blog_lists)

            for list in reader:
                result.append(list)

        return JsonResponse({'search list' : result}, status=200)



      # return JsonResponse({'search list' : list(SearchList.objects.values())}, status=200)

