from django.urls import path
from .views import*


urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('contact-us', ContactCreateView.as_view(), name='contact'),
    path('contact-list', ContactListView.as_view(), name='contact_list'),
    path('contact-update/<int:pk>', ContactUpdateView.as_view(), name='update_contact'),
    path('contact-delete/<int:pk>/delete/', ContactDeleteView.as_view(), name='delete_contact'),
]
