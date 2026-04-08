

# # calc/urls.py
# from django.urls import path
# from .views.menu.category_views import CategoryListCreateView
# from .views.menu.category_detail_view import CategoryDetailView
# from .views.menu.item_views import ItemListCreateView
# from .views.menu.item_detail_views import ItemDetailView 
# from .views.auth.register_views import RegisterView
# from .views.auth.login_views import LoginView
# from .views.home.about.about_views import AboutDetailView, AboutView

# urlpatterns = [
#     path('categories', CategoryListCreateView.as_view(), name='category-list'),
#     path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
#     path('items/<int:category_id>/', ItemListCreateView.as_view(), name='item-list'),
#       path('item/<int:id>/', ItemDetailView.as_view(), name='item-detail'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('about', AboutView.as_view(), name='about'), 
#     path('about/<int:id>/', AboutDetailView.as_view(), name='about-detail'), 

    
# ]







from django.urls import path
from .views.menu.category_views import CategoryListCreateView
from .views.menu.category_detail_view import CategoryDetailView
from .views.menu.item_views import ItemListCreateView
from .views.menu.item_detail_views import ItemDetailView 
from .views.auth.register_views import RegisterView
from .views.auth.login_views import LoginView
from .views.home.about.about_views import AboutDetailView, AboutView


urlpatterns = [
    path('categories', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('items/<int:category_id>/', ItemListCreateView.as_view(), name='item-list'),
    path('item/<int:id>/', ItemDetailView.as_view(), name='item-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('about', AboutView.as_view(), name='about'), 
    path('about/<int:id>/', AboutDetailView.as_view(), name='about-detail'), 
]





