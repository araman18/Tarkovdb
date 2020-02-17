from django.urls import path

from . import views

app_name = 'tarkovdb'

urlpatterns = [
    # ex: /polls/
    path('all', views.index, name='index'),
    path('maps', views.maps, name='maps'),
    path('',views.add,name='add'),
    path('<int:item_id>/', views.detail, name='detail'),

]