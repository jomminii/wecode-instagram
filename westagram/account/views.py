import json
import bcrypt
import jwt

from my_settings import SECRET_KEY 
from .models import Account

from django.views import View
from django.http import JsonResponse, HttpResponse

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email = data['email']).exists():  # 존재하는 이메일인지 확인
                return HttpResponse(status=400) 
                
            #== 비밀번호 암호화==#    
            
            password = data['password'].encode('utf-8')                 # 입력된 패스워드를 바이트 형태로 인코딩
            password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())  # 암호화된 비밀번호 생성
            password_crypt = password_crypt.decode('utf-8')             # DB에 저장할 수 있는 유니코드 문자열 형태로 디코딩
            
            #====================#
            
            Account(
                email    = data['email'],
                password = password_crypt                               # 암호화된 비밀번호를 DB에 저장
            ).save()
       
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Account.objects.filter(email = data['email']).exists() :
                user = Account.objects.get(email = data['email'])
           
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')) :
                   
                    #----------토큰 발행----------#
                   
                    token = jwt.encode({'email' : data['email']}, SECRET_KEY, algorithm = "HS256")
                    token = token.decode('utf-8')      # 유니코드 문자열로 디코딩

                    #-----------------------------#
                    return JsonResponse({"token" : token }, status=200)
           
                else :
                    return HttpResponse(status=401)

            return HttpResponse(status=400)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 400)                                  



class TokenCheckView(View):
    def post(self,request):
        data = json.loads(request.body)

        user_token_info = jwt.decode(data['token'], SECRET_KEY, algorithm = 'HS256')

        if Account.objects.filter(email=user_token_info['email']).exists() :
            return HttpResponse(status=200)
        
        return HttpResponse(status=403)

