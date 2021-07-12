from django.contrib import admin
from .models import Person, Citizenship, Language, Room, Gallery
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    list_filter = ('is_verify',)


admin.site.register(Person, PersonAdmin)

admin.site.register(Citizenship)
admin.site.register(Language)
admin.site.register(Room)
admin.site.register(Gallery)
