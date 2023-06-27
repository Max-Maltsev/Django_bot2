from django.contrib import admin
from telegram_bot_app.models import Prod, Users, Call, History
admin.site.register(Prod)
admin.site.register(Users)
admin.site.register(Call)
admin.site.register(History)
# Register your models here.
