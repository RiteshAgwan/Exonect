from celery import shared_task
from django.core.mail import send_mail
from .models import Product

@shared_task
def send_product_notification(product_id):
    product = Product.objects.get(id=product_id)
    subject = f'New Product Alert: {product.name}'
    message = f'Check out our new product: {product.name}\nPrice: {product.price}\nDescription: {product.description}'
    recipient_list = ['customer@example.com']  # Replace with actual recipient list
    send_mail(subject, message, 'from@example.com', recipient_list)

@shared_task
def update_product_stock(product_id, quantity):
    product = Product.objects.get(id=product_id)
    product.stock += quantity
    product.save()