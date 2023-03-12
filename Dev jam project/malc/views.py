from django.shortcuts import render
from  .models import destination
# Create your views here.
def index(request):
   
   dests = destination.objects.all()

    
   return render (request, "ind2.html", {'dests': dests})

def review(request):

   return render (request, "review.html")