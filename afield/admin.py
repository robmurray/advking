from django.contrib import admin
from django import forms
from .models import Room, RoomAction


class ChoiceInline(admin.TabularInline):
    model = RoomAction
    extra = 3


class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Description', {'fields': ['description']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('id', 'name')
    search_fields = ['id','name']


admin.site.register(Room,RoomAdmin)

'''
class RoomModelForm( forms.ModelForm ):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Room
'''