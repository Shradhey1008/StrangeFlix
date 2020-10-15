from django.db import models
# from django.contrib.auth import settings
from django.conf import settings
from django.db.models.signals import post_save
import razorpay


Membership_Choices = (
    ('Basic','basic'),
    ('Standard','std'),
    ('Premium','prem'),
)

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_SECRET_KEY))

order_amount = 100
order_currency = 'INR'
order_receipt = 'order-rcptid-11'
notes = {'Shipping address': 'Allahabad,UttarPradesh'}

class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(choices=Membership_Choices,default='basic',max_length=30)
    price = models.IntegerField(default=15)
    razorpay_id = models.CharField(max_length=50)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    razorpay_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Membership,on_delete=models.SET_NULL,null= True)

    def __str__(self):
        return self.user.username


def post_save_usermembership_create(sender, instance, created,*args,**kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)
    
    user_membership, created = UserMembership.objects.get_or_create(user = instance)

    print(user_membership.razorpay_customer_id)
    if user_membership.razorpay_customer_id is None or user_membership.razorpay_customer_id == '':
        # new_customer_id = client.order.create(dict(amount=order_amount,currency=order_currency,receipt=order_receipt,notes=notes,payment_capture='0'))
        new_customer_id = client.customer.create(dict(name=instance.username,contact=7393011475,email = instance.email))
        print(new_customer_id)
        user_membership.razorpay_customer_id = new_customer_id['id']
        user_membership.save()

post_save.connect(post_save_usermembership_create,sender=settings.AUTH_USER_MODEL)


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    razorpay_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username