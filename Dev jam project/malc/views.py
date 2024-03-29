from django.shortcuts import render,redirect,get_object_or_404
from  .models import Reviews
from .forms import ReviewForm,FeedbackForm
# Create your views here.
def index(request):
    
    return render (request, "ind2.html")

def about(request):
   return render (request, "about.html")
   
def review(request):
  reviews=Reviews.objects
  if request.method=="GET":
  
   st=request.GET.get('searchname')
   if st!=None:
      reviews=Reviews.objects.filter(title__icontains=st)
  
  return render (request, "seereview.html", {'reviews':reviews})

def locationreview(request, review_id):
   
   review_detail = get_object_or_404(Reviews,pk = review_id)
   review=Reviews.objects.get(id=review_id)
   title= review.title
   author = review.author
   body = review.body
   image= review.image
    
   context={'review':review,'title':title,'author':author,'body':body,'image':image}
   return render(request,"locationreview.html",context)





def submitreview(request):
   
   
   form = ReviewForm()
   if request.method == 'POST':
      form = ReviewForm(request.POST,request.FILES)
      if form.is_valid():
         review = form.save(commit=False)
         review.author = request.user
         review.save()
         print('form submitted')

         return render (request,'logout2.html')
      
      else:
         
         form = ReviewForm()
        
   return render(request,'review.html',{'form':form})


def submitfeedback(request):
   
   
   form = FeedbackForm()
   if request.method == 'POST':
      form = FeedbackForm(request.POST,request.FILES)
      if form.is_valid():
         feedback = form.save(commit=False)
         feedback.author = request.user
         feedback.save()
         print('form submitted')

         return render (request,'logout2.html')
      
      else:
         
         form = FeedbackForm()
        
   return render(request,'star.html',{'form':form})

def loginpage(request):
   return render(request,'login.html')