from django.contrib import admin

# Register your models here.
from .models import Question,Suit


admin.site.register(Question)
admin.site.register(Suit)