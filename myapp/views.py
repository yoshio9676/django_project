from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

# function based view
def helloworldFunction(request):
    object = HttpResponse('<h1>hello, world!!!!</h1>')
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