from django.http import HttpResponse

def index(request):
        return HttpResponse("Hello i a django app")