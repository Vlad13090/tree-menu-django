from django.urls import path
from menuApp.views import draw_menu

app_name = 'menuApp'

urlpatterns = [
    path('<str:menu_name>/', draw_menu, name='draw_menu'),
]