from django.urls import path 


from . import views

urlpatterns =[ path('',views.index, name='index'),
                                   
               path('submitreview',views.submitreview,name='submitreview') ,
               path('review' ,views.review,name='review'),
               path('<int:review_id>/',views.locationreview,name='locationreview'),
               path('about',views.about,name='about')   ]