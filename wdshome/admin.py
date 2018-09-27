from django.contrib import admin
from .models import Annonser, Brukerinformasjon, Utviklere, Emne, Annonse_emne

admin.site.register(Annonser)
admin.site.register(Brukerinformasjon)
admin.site.register(Utviklere)
admin.site.register(Emne)
admin.site.register(Annonse_emne)
