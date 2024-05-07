# churn_pred/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.predict_churn, name='predict_churn'),
    path('predictions/', views.list_predictions, name='prediction_list'),
]
