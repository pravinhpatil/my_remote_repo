from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view(request):
   return render(request, 'testApp/wish.html')
