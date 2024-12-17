from django.contrib import admin
from django.utils.timezone import now
from contact.models import Contacts
from django import forms

class contactModelForm( forms.ModelForm ):
    answer = forms.CharField( widget=forms.Textarea )
    # class Meta:
    #     model = Contacts
    #     fields = []


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at', "answered_at", 'answer')
    search_fields = ('name', 'email', 'phone', 'message', 'created_at', "answered_at")
    
    form = contactModelForm

    def contacted_today(self, obj):
        return obj.created_at.date() == now().date()
    
    contacted_today.short_description = 'Contatou hoje?'
    contacted_today.boolean = True

    # contacted_today.short_description = 'Contatou hoje?'
    # # contacted_today.boolean = True




admin.site.register(Contacts, ContactModelAdmin)


