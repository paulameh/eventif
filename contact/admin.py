from django.contrib import admin
from django.utils.timezone import now
from contact.models import Contacts



class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    
    # date_hierarchy = 'created_at'
    # search_fields = ('name', 'email', 'phone', 'message', 'created_at', 'answered_at','flag')
    # list_filter = ('created_at', 'answered_at','flag')
    # actions = ['answer',]

    # def contacted_today(self, obj):
    #     return obj.created_at.date() == now().date()

    # contacted_today.short_description = 'Contatou hoje?'
    # contacted_today.boolean = True




admin.site.register(Contacts, ContactModelAdmin)


