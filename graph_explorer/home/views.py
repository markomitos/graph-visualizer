from django.shortcuts import HttpResponse, render

from app_platform.app_platform import main
# Create your views here.
def home(request):
    plugins = main()
    return render(request,"index.html",{"title":"Index"})
