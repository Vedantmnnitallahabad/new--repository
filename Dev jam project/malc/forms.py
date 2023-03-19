
from django import forms
from .models import  Reviews,Feedbacks


class ReviewForm(forms.ModelForm):


    class Meta:
        model = Reviews
        fields = ['title','body','criticR','image']

class FeedbackForm(forms.ModelForm):        
     


    class Meta:
          model= Feedbacks
          fields= ['rate','body']
    