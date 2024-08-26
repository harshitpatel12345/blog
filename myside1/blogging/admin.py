from django.contrib import admin
from blogging.models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(Payment)
admin.site.register(Plan)
