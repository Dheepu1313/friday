from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")
def home(request):
    return render (request, 'home.html')
   
   
   
   

 