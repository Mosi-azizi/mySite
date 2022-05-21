from django.contrib import admin
from .models import Profile,Skill,Message,Education,Employment
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['__str__','subject','is_read']
    # list_editable = ['is_read']

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message,MessageAdmin)
admin.site.register(Education)
admin.site.register(Employment)

