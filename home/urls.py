from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name="Home"),
    path('Home/', views.home, name="Home"),
    path('faq/', views.faq,name="faq"),
    path('faq/Login', views.Login, name='Login'),
    path('faq/Logout', views.Logout,name='Logout'),
    
    path('mbplan/', views.mbplan,name="mbplan"),

    path('EndowmentPlan/faq', views.faq ),
    path('ChildPlan/faq', views.faq ),
    path('MoneyBack/faq', views.faq ),


    path('Login/Home/Logout', views.home, name="Home"),
    path('Login/', views.Login ,name='Login'),
    path('Login/upload', views.bond ,name='upload'),
    path('Login/Login', views.Login ,name='Login'),
    path('Login/User', views.User ,name='User'),
    path('Login/Pupload', views.pupload ,name='pupload'),

    path('Logout/', views.Logout,name='Logout'),
    path('Login/Logout/', views.Logout,name='Logout'),

    path('ChildPlan/Child.html', views.Child, name="Child"),
    path('EndowmentPlan/endplans.html', views.Endowment, name="Endowment"),
    path('HealthPlan/Health.html', views.Health, name="Health"),
    path('MoneyBack/MoneyBack.html', views.MoneyBack, name="MoneyBack"),
    path('Pensionplan/Pension.html', views.Pension, name="Pension"),

]
