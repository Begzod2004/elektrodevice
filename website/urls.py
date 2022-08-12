from django.urls import path
from .views import *
from .workview import Workplace,Check

urlpatterns = [
    # path('', IndexView,name="index"), 
    path('about/', Aboutus_View,name="about"),
    path('contacts/', Contacts_View,name="contacts"),
    path('service/', Services_View,name="service"),
    path('news/', NewListView.as_view(),name="new"),
    path('detailednew/', Detailed_News,name="detailednew"),
    path('portfolio/', Portfolio,name="portfolio"),
    path('workplace/',Workplace,name="workplace"),
    path('check/',Check,name="check"),
    # Yangi qo'shilgan narsalar!
    path('', OrganizationListView.as_view(), name='index'),
    path('New/<int:pk>', NewDetailView.as_view(), name='NewDetailView'),
    path('Organization/<int:pk>', OrgnizationDetailView.as_view(), name='OrganizationDetailView'),
    path('register/', user_register_view, name='register'),
    path('login/', user_login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('registeratsiya/', profile, name='registeratsiya'),


]