from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Membership, UserMembership, Subscription, stripe
from django.conf import settings
from json import dumps

# Create your views here.

def membership(request):
    plans = Membership.objects.all().order_by('price')
    current_membership = get_user_membership(request)

    context = {'objects': plans, 'current_membership': str(
        current_membership.membership)}
    return render(request, 'memberships.html', context)


def selected_plan(request):
    selected_membership_type = request.POST.get('membership_type')

    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)
    selected_membership_qs = Membership.objects.filter(
        membership_type=selected_membership_type)

    """
    ==========
    VALIDATION
    ==========
    """
    if selected_membership_qs.exists():
        selected_membership = selected_membership_qs.first()

    if user_membership.membership == selected_membership:
        if user_subscription == None:
            context['messages'] = 'You already have this plan'
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # assign membership type to session so that it can be accessed in next view
    request.session['selected_membership_type'] = selected_membership.membership_type
    return HttpResponseRedirect(reverse('subscriptions:payment'))


def PaymentView(request):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)

    publish_key = settings.STRIPE_KEY_ID

    if request.method == "POST":
        try:
            token = request.POST['stripeToken']
            cus = stripe.Customer.retrieve(user_membership.stripe_customer_id)
            cus.source = token
            cus.save()
            subscription = stripe.Subscription.create(
                customer=user_membership.stripe_customer_id,
                items=[
                    {
                        "price": selected_membership.stripe_id,
                    },
                ],
            )
            return redirect(reverse('subscriptions:update', kwargs={
                'Subscription_id': subscription.id,
            }))
        except stripe.error.CardError as e:
            messages.info(request, "Your card has declined")

    context = {
        'publish_key': publish_key,
        'selected_membership': selected_membership,
        'price': selected_membership.price,
    }
    return render(request, 'checkout.html', context)


def updateTransactions(request, Subscription_id):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)
    user_membership.membership = selected_membership
    user_membership.save()

    sub, created = Subscription.objects.get_or_create(
        user_membership=user_membership)
    sub.stripe_subscription_id = Subscription_id
    sub.active = True
    sub.save()

    try:
        del request.session['selected_membership_type']
    except:
        pass

    messages.info(request, "Successfully created membership")
    return redirect('/')


def cancelSubscription(request):
    user_sub = get_user_subscription(request)

    if user_sub.active == False:
        messages.info(request,"You dont have an active Membership")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    sub = stripe.Subscription.retrieve(user_sub.stripe_subscription_id)
    sub.delete()

    user_sub.user_membership.membership.membership_type = None 
    user_sub.active = False
    user_sub.save()

    free_membership = Membership.objects.filter(membership_type='Basic').first()
    user_membership = get_user_membership(request)
    user_membership.membership = free_membership
    user_membership.save()

    messages.info(request, "Successfully cancelled membership.")
    return redirect('/profile')


def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(
        user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


def get_selected_membership(request):
    membership_type = request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(
        membership_type=membership_type)

    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None
