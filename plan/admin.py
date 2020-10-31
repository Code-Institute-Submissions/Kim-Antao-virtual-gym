from django.contrib import admin

from .models import Plan, Subscription, Service, SubscriberRegistration

admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(Service)
admin.site.register(SubscriberRegistration)
