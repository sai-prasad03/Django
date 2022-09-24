from django.urls import path
from .import views

urlpatterns = [
    path('learndj/',views.learn_Django),
    # path('learnpy/',views.learn_python),
    # path('dtt/',views.Date_time),
    # path('nm/',views.Names),
    
]