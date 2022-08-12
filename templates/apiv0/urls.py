from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    path('test-api-view/', test_api_view),
    path('Technique-api-view/', TechniqueListAPIView.as_view()),
    path('Technique-api-view/create', TechniqueCreateAPIView.as_view()),
    path('Technique-api-view/update/<int:pk>', TechniqueUpdateAPIView.as_view()),
    path('Technique-api-view/delete/<int:pk>', TechniqueDestroyAPIView.as_view()),
    
    path('Technique-api-view/<int:pk>/', Technique_api_view),path('test-api-view/', test_api_view),
    
    path('Brand-api-view/', BrandListAPIView.as_view()),
    path('Brand-api-view/create', BrandCreateAPIView.as_view()),
    path('Brand-api-view/update/<int:pk>', BrandUpdateAPIView.as_view()),
    path('Brand-api-view/delete/<int:pk>', BrandDestroyAPIView.as_view()),
    path('Brand-api-view/<int:pk>/', Brand_api_view),
    
    
    path('Size-api-view/', SizeListAPIView.as_view()),
    path('Size-api-view/create', SizeCreateAPIView.as_view()),
    path('Size-api-view/update/<int:pk>', SizeUpdateAPIView.as_view()),
    path('Size-api-view/delete/<int:pk>', SizeDestroyAPIView.as_view()),
    
    path('Size-api-view/<int:pk>/', Size_api_view),
    

    path('Company-api-view/', CompanyListAPIView.as_view()),
    path('Company-api-view/create', CompanyCreateAPIView.as_view()),
    path('Company-api-view/update/<int:pk>', CompanyUpdateAPIView.as_view()),
    path('Company-api-view/delete/<int:pk>', CompanyDestroyAPIView.as_view()),
    
    path('Company-api-view/<int:pk>/', Company_api_view),

    
    path('Aksiya-api-view/', AksiyaListAPIView.as_view()),
    path('Aksiya-api-view/create', AksiyaCreateAPIView.as_view()),
    path('Aksiya-api-view/update/<int:pk>', AksiyaUpdateAPIView.as_view()),
    path('Aksiya-api-view/delete/<int:pk>', AksiyaDestroyAPIView.as_view()),
    
    path('Aksiya-api-view/<int:pk>/', Aksiya_api_view),

    

    path('auth/', include('rest_framework.urls')),

]

