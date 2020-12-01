from django.urls import path, include
from tutorials import views 

urlpatterns = [ 
    path('tutorials/', views.tutorial_list),
    path('tutorials/', views.tutorial_detail),
    path('tutorials/', views.tutorial_list_published),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

