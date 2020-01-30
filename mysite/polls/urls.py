from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2',views.table,name="index2"),
    path('crud/',  views.CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/update/',  views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
]