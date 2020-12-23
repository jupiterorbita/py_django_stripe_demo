from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse

import stripe


def index(request):
  return render(request, 'index.html')

def thanks(request):
  return render(request, 'thanks.html')

# method for creating session for stripe for cart
def checkout(request):
  # cross site request forgery tokens
  stripe.api_key = settings.STRIPE_PRIVATE_KEY
  
  session = stripe.checkout.Session.create(
    payment_method_types = ['card'],
    line_items=[{
      'price': 'price_1I1NieBtJ7xCB34pIj3O0jRy',
      'quantity': 1
    }],
    mode='payment',
    success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
    cancel_url=request.build_absolute_uri(reverse('index')),
    )
  return JsonResponse({
    'session_id': session.id,
    'stripe_public_key': settings.STRIPE_PUBLIC_KEY
  })
  
# stripe web-hook
# let stripe redirect to success if payment was successful
def stripe_webhook(request):
  pass