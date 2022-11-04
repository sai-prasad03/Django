from django.urls import path
from . import views
urlpatterns = [

    path('register/',views.ShowFormData),
    path('success/', views.thankyou)
]