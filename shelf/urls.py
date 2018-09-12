from django.urls import path
from . import views

urlpatterns = [
    path('', views.treasure_list, name='treasure_list'),
    path('treasures/<int:pk>', views.treasure_detail, name='treasure_detail'),
    path('treasures/new', views.treasure_create, name='treasure_create'),
    path('treasures/<int:pk>/edit', views.treasure_edit, name='treasure_edit'),
    path('treasures/<int:pk>/delete', views.treasure_delete, name='treasure_delete'),
    path('accounts/signup/', views.sign_up, name='signup'),

    path('treasures_file/<int:pk>', views.file_treasure_detail, name='file_treasure_detail'),
    path('treasures_file/new', views.file_treasure_create, name='file_treasure_create'),
]
