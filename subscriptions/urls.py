from django.urls import path

from . import views

app_name = 'subscriptions'
urlpatterns = [
    path('',views.membership,name = 'select'),
    path('plan/',views.selected_plan,name = 'plan'),
    path('plan/payment/',views.PaymentView,name = 'payment'),
    path('plan/payment/update/<Subscription_id>/',views.updateTransactions,name = 'update'),
]