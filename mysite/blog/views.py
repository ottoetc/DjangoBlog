from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, blog. Welcome to Nathan's Dev Blog")
