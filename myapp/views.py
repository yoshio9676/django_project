from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from pathlib import Path


# function based view
def helloworldFunction(request):
    path = Path(__file__).resolve().parent.parent
    object = HttpResponse(path)
    return object

def helloJsonResponse(request):
    return JsonResponse({
        'name': 'yoshimasa',
        'age': 27,
        'email': 'yoshimasa@gmail.com'
    })
    

# class based view
class HelloWorldClass(TemplateView):
    template_name = "hello.html" # どのHTMLファイルを持ってくるか