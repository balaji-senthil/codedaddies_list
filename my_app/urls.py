#cutom urls
from django.urls import path
from . import views

urlpatterns=[
    path=('',views.home,name='home'),
    #path('admin/',admin.site.urls),
]