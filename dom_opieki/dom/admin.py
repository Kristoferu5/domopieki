from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Lekarz)
admin.site.register(Pensjonariusz)
admin.site.register(HistoriaLeczenia)
admin.site.register(Recepty)



