from django.db import models
# from django.contrib.auth import settings
from django.conf import settings
from django.db.models.signals import post_save
import stripe
from datetime import datetime


Membership_Choices = (
    ('Basic','basic'),
    ('Standard','std'),
    ('Premium','prem'),
)
stripe.api_key = settings.STRIPE_SECRET_KEY


# This model creates Memberships of different subscription plans
class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(choices=Membership_Choices,default='basic',max_length=30)
    price = models.IntegerField(default=15)
    stripe_id = models.CharField(max_length=50,default=None)

    def __str__(self):
        return self.membership_type

# This Model saves the membership of the current User
class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Membership,on_delete=models.SET_NULL,null= True)

    def __str__(self):
        return self.user.username


# this is a signal function to create stripe customer of the current user
def post_save_usermembership_create(sender, instance, created,*args,**kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)
    
    user_membership, created = UserMembership.objects.get_or_create(user = instance)
    if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id == '':
        new_customer_id = stripe.Customer.create(email=instance.email)
        user_membership.stripe_customer_id = new_customer_id['id']
        user_membership.save()

post_save.connect(post_save_usermembership_create,sender=settings.AUTH_USER_MODEL)

# This model saves subscription taken by different Users of different plans
class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username

    @property
    def get_created_date(self):
        subscription = stripe.Subscription.retrieve(self.stripe_subscription_id)
        return datetime.fromtimestamp(subscription.created)
    
    def get_next_billing_date(self):
        subscription = stripe.Subscription.retrieve(self.stripe_subscription_id)
        return datetime.fromtimestamp(subscription.current_period_end)
        
