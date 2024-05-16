from django.contrib import admin
from .models import Sitter, Baby, Payment, ProcurementItem, Activity, Notification

admin.site.register(Sitter)
admin.site.register(Baby)
admin.site.register(Payment)
admin.site.register(ProcurementItem)
admin.site.register(Activity)
admin.site.register(Notification)