# inference/urls.py
from django.urls import path
from .views import s2st, s2tt, t2st, t2tt, asr

urlpatterns = [
    path('s2st/', s2st, name='s2st'),
    path('s2tt/', s2tt, name='s2tt'),
    path('t2st/', t2st, name='t2st'),
    path('t2tt/', t2tt, name='t2tt'),
    path('asr/', asr, name='asr'),
]
