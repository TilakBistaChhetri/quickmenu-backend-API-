

# # calc/urls.py
# from django.urls import path

# from calc.views.menu.views import CategoryDetailView
# from .views.auth.register_views import RegisterView
# from .views.auth.login_views import LoginView
# from .views.menu.category_views import CategoryListCreateView
# from .views.menu.item_views import ItemListCreateView

# urlpatterns = [
#     path('categories', CategoryListCreateView.as_view(), name='category-list'),
#     path('items', ItemListCreateView.as_view(), name='item-list'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
# ]





# calc/urls.py
from django.urls import path
from .views.menu.category_views import CategoryListCreateView
from .views.menu.category_detail_view import CategoryDetailView
from .views.menu.item_views import ItemListCreateView
from .views.auth.register_views import RegisterView
from .views.auth.login_views import LoginView

urlpatterns = [
    path('categories', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('items', ItemListCreateView.as_view(), name='item-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
