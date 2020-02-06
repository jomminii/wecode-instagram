import json
from .models import Account
from django.views import View
from django.http import JsonResponse, HttpResponse

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        Account(
            email    = data['email'],
            password = data['password']
        ).save()

        # return HttpResponse(status=200)
        return JsonResponse({'message':'회원가입 완료염'},status=200)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        

        if Account.objects.filter(email = data['email']).exists() :
            user = Account.objects.get(email = data['email'])
            if user.password == data['password'] :
                    return JsonResponse({'message':f'{user.email}님 로그인 성공쓰'},status=200)
            else :
                    return JsonResponse({'message':'비밀번호 좀 외워줘'},status=200)
        return JsonResponse({'message':'그런 이메일은 존재하지 않아 친구야'},status=200)



# for문을 사용해서 만들었으나, 쓸데없이 전체 데이터를 도니까 위처럼 바꿈
        #for account in Account.objects.values():
         #   if account['email'] == data['email']:
          #      if account['password'] == data['password'] :
           #         return JsonResponse({'message':'login success'},status=200)
            #    else :
             #       return JsonResponse({'message':'login failure. wrong password'},status=200)
            
       # return JsonResponse({'message':'login failure. wrong email'},status=200)
