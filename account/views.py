import json

from .models import Account

from django.views import View
from django.http import JsonResponse, HttpResponse

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        if Account.objects.filter(email = data['email']).exists(): # 존재하는 이메일인지 확인
            return HttpResponse(status=400) 

        Account(
            email    = data['email'],
            password = data['password']
        ).save()
       
        return HttpResponse(status=200)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Account.objects.filter(email = data['email']).exists() :
                user = Account.objects.get(email = data['email'])
           
                if user.password == data['password'] :
                    return HttpResponse(status=200)
           
                else :
                    return HttpResponse(status=401)

            return HttpResponse(status=400)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 400)                                  


# for문을 사용해서 만들었으나, 쓸데없이 전체 데이터를 도니까 위처럼 바꿈
        #for account in Account.objects.values():
         #   if account['email'] == data['email']:
          #      if account['password'] == data['password'] :
           #         return JsonResponse({'message':'login success'},status=200)
            #    else :
             #       return JsonResponse({'message':'login failure. wrong password'},status=200)
            
       # return JsonResponse({'message':'login failure. wrong email'},status=200)
