from django.contrib import admin
from . models import Super
# Register your models here.
class SuperAdmin(admin.ModelAdmin):
    class Meta:
     
        list_display = (
            'id',
            'name',
            'email',
            'gender',
            'mobile',
            'dob',
            'state',
            'city',
            'pin',
            'profile_image',
            'file',
        )

        def __str__(self):
            return self.name

admin.site.register(Super)