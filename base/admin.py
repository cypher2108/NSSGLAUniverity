from django.contrib import admin

# Register your models here.
from base.models import Applicant, Contact, Event, Post, Blog

admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(Applicant)
