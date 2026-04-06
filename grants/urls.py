from django.urls import path
from . import views

app_name = 'grants'

urlpatterns = [
    path('', views.GrantApplicationCreateView.as_view(), name='application_create'),
    path('application/', views.GrantApplicationDetailView.as_view(), name='application_detail'),
    path('application/edit/', views.GrantApplicationUpdateView.as_view(), name='application_update'),
] 