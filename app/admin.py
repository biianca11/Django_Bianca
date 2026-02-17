# Register your models here.
from django.contrib import admin
from .models import Topping, Pizza, Proovedor

admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Proovedor)