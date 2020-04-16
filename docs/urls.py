from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from docs import views

urlpatterns = [
    path('docs/', views.DocumentList.as_view()),
    path('docs/<int:pk>/', views.DocumentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)