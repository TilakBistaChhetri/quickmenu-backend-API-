



from django.urls import path


from .views.contact_details_views import ContactDetailsView
from .views.contact_views import ContactListCreateView
from .views.category_views import CategoryListCreateView
from .views.category_detail_views import CategoryDetailView
from .views.item_views import ItemListCreateView
from .views.item_detail_views import ItemDetailView
from .views.register_views import RegisterView
from .views.login_views import LoginView
from .views.about_views import AboutDetailView, AboutView


urlpatterns = [
    path('categories', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('items/<int:category_id>/', ItemListCreateView.as_view(), name='item-list'),
    path('item/<int:id>/', ItemDetailView.as_view(), name='item-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('about', AboutView.as_view(), name='about'), 
    path('about/<int:id>/', AboutDetailView.as_view(), name='about-detail'), 
    path('contact', ContactListCreateView.as_view(), name='contact-list-create'),
  
 
   path('contact/<int:id>/', ContactDetailsView.as_view(), name='contact-detail')

]















