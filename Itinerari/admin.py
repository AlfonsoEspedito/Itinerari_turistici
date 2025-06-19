from django.contrib import admin

from .models import Lingua, Amministratore, Turista, Tappa, Guida, Itinerario, Feedback, Visita, Prenotazione

admin.site.register(Lingua)
admin.site.register(Amministratore)
admin.site.register(Tappa)
admin.site.register(Guida)
admin.site.register(Itinerario)
admin.site.register(Feedback)
admin.site.register(Visita)
admin.site.register(Prenotazione)


