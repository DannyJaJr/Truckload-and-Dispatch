from django.contrib import admin

from .models import Load, Category, Message, PhoneNumber

# Register your models here.
admin.site.register(Load)
admin.site.register(Category)
admin.site.register(PhoneNumber)


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'score']

admin.site.register(Message, MessageAdmin)




