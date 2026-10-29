import time
from celery import shared_task

@shared_task(name='apps.testapp.tasks.send_welcome_email_task')
def send_welcome_email_task(user_email):
    time.sleep(5)
    print(f"Welcome email sent to {user_email}")
    return f"Welcome email sent to {user_email}"

@shared_task(name='apps.testapp.tasks.clear_expired_cache_task')
def clear_expired_cache_task():
    print("Beat Task: Cleaning expired items...")
    return "Beat Task: Cleaning expired items..."
