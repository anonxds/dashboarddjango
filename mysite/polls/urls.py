from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buttons',views.buttons,name="buttons"),
    path('tables/',views.get_info.as_view(),name="more_info")
]