from django.urls import path
from . import views 
from .import context_processor_file

app_name = 'mainUser'

urlpatterns = [
    path('',views.getCarsView,name = 'mainPage'),
    path('print/<username>/', views.print_from_button ,name='printButton'),
    path('ajax', views.answer_me, name='get_response'),
    path('auth', views.authUser, name='authUser'),
    path('logout', views.logout_req, name='logout'),
    path('ajax_conPro', context_processor_file.returnTimeNow, name='ajax_conPro'),
]
