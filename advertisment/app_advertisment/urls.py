from django.urls import path
from .views import index, top_sellers, advertisement_post, profile, login, register

urlpatterns = [
    path('', index, name='main_page'),
    path('top-sellers/', top_sellers, name='top_sellers'),
    path('advertisement_post/', advertisement_post, name='adv_post'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]