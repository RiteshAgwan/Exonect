from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def send_order_confirmation_email(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order Confirmation'
    message = f'Thank you for your order, {order.user.username}! Your order ID is {order.id}.'
    recipient_list = [order.user.email]
    send_mail(subject, message, 'from@example.com', recipient_list)

@shared_task
def generate_order_report():
    # Logic to generate a report of orders
    pass

@shared_task
def process_order(order_id):
    # Logic to process the order
    pass