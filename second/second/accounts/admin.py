from django.contrib import admin
from .models import Person
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    list_filter = ('is_verify',)


admin.site.register(Person, PersonAdmin)
