from django.contrib import admin
from .models import detail

# Register your models here.
class detailadmin(admin.ModelAdmin):
    list_display=('name','phone','message',)

admin.site.register(detail,detailadmin)