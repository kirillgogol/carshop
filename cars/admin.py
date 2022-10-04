from re import search
from django.contrib import admin

from .models import Car, TechSpec, Comment
from django.contrib.auth.models import User

class TechSpecInLine(admin.StackedInline):
    model = TechSpec
    extra = 0


class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Car', {'fields': ['brand', 'car_model']}),
        ('Specifications', {'fields': ['color', 'year', 'photo', 'cost']})
    ]
    inlines = [TechSpecInLine]


class UserInLine(admin.StackedInline):
    model = User


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Comment', {'fields': ['header', 'body', 'active', 'car', 'user']})
    ]

admin.site.register(Car, CarAdmin)
admin.site.register(Comment, CommentAdmin)
