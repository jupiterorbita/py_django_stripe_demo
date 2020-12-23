from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/', views.thanks, name='thanks'),
    path('checkout/', views.checkout, name='checkout'),
    path('stripe_webhook', views.stripe_webhook, name="stripe_webhook"),
]

# STRIPE CLI
# stripe listen --forward-to localhost:8000/stripe_webhook/