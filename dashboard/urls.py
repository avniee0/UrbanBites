from django.urls import path
from . import views
from core import views as core_views


urlpatterns = [

    path('', views.dashboard_home, name='dashboard'),

    path('logout/', core_views.logout_user, name='logout'),

    path('update-order/<int:id>/',views.update_order_status,name='update_order_status'),

    path('menu/', views.menu_manage, name='menu_manage'),

    path('add-item/',views.add_menu_item,name='add_menu_item'),

    path('edit-item/<int:id>/',views.edit_menu_item,name='edit_menu_item'),

    path('delete-item/<int:id>/',views.delete_menu_item, name='delete_menu_item'),

    path('orders/',views.order_manage,name='order_manage'),
]

