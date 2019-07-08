from django.utils.deprecation import MiddlewareMixin

class MyMiddel(MiddlewareMixin):
    def process_request(self,request):
        print("get aget get: " , request.GET.get('a'))