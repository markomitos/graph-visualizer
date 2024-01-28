from django.shortcuts import HttpResponse

from app_platform.app_platform import main
# Create your views here.
def home(request):
    plugins = main()
    return HttpResponse('Hello World')
