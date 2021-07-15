from django.contrib import admin
from .models import uregi

@admin.register(uregi)
class uregi_admin(admin.ModelAdmin):
    list_display=['id','name','dob','gender','locality','city','pin','state','mobile','email','job','profile_image','doc']
