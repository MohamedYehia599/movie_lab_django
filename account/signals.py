from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.dispatch import receiver
# @receiver(post_save,sender=User)
# def user_post_save_action(**kwargs):
#     if(kwargs.get('created')):
#         user = kwargs.get('instance')
#         print(f'user : {user.email}')
#         subj= 'Welcome !!'
#         msg = f'welcome {user}'
#         receivers=[user.email]
#         send_mail(subject=subj,message=msg,from_email='test.test1233345@gmail.com',recipient_list=receivers)