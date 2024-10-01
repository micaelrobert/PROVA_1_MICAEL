from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à minha app</h1>")
