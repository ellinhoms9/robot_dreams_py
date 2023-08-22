from celery import shared_task
from users.models import Users
from purchase.models import Purchases


@shared_task
def print_hello_world():
    print("Some text from users task")


@shared_task
def print_purchase_count(user_id):
    user = Users.objects.get(id=user_id)
    purchase_count = Purchases.objects.filter(user=user).count()
    print(f"Purchase count for user {user.username}: {purchase_count}")


@shared_task
def print_user_count():
    user_count = Users.objects.count()
    print(f"Number of users in the database: {user_count}")
