from django.urls import path
from . import views
from .views import NewsDetail

urlpatterns = [
    path('news/', views.home, name='newslist-home'),
    path('about/', views.about, name='about-portal'),
    # path('news/<int:pk>', views.news, name=''),
    path('news/<int:pk>', NewsDetail.as_view()),
]
