from django.urls import path
from .views import home, thread_detail, post_detail, new_thread,new_post, search_for_thread

urlpatterns = [
    path('', home, name='home'),
    path('thread/<slug:slug>/', thread_detail, name='thread_detail'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('new_thread/', new_thread, name='new_thread'),
    path('thread/<slug:thread_slug>/new_post/', new_post, name='new_post'),
    path('search/', search_for_thread, name='search_for_thread'),
]
