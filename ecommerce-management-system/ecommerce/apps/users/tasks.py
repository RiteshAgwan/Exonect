from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(user_email):
    subject = 'Welcome to Our E-commerce Platform'
    message = 'Thank you for registering with us!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    
    send_mail(subject, message, from_email, recipient_list)

@shared_task
def generate_user_report(user_id):
    # Logic to generate a report for the user
    pass

@shared_task
def notify_user_of_order_status(user_email, order_status):
    subject = 'Order Status Update'
    message = f'Your order status has been updated to: {order_status}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    
    send_mail(subject, message, from_email, recipient_list)