from celery import shared_task
from django.contrib.auth import get_user_model

@shared_task(bind=True)
def My_Work(self):
    #operations
    for i in "bhushan":
        print(i)
    return "Done"



@shared_task(bind=True)
def Good_morning(self):

    for i in range(10):
        print(i)
    
    return "Good Morning"