from django.urls import path
from .views import ListCategoryApiView, ListRoadSignsApiView, DetailRoadSignsApiView


urlpatterns = [
    path('category/', ListCategoryApiView.as_view(), name='category'),
    path('roadsigns/', ListRoadSignsApiView.as_view(), name='roadsigns'),
    path('roadsigns/<int:pk>/', DetailRoadSignsApiView.as_view(), name='roadsigns_detail'),
]
