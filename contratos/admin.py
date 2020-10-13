from django.contrib import admin
from contratos.models import Contrato, Aditivo

# Register your models here.
#admin.site.register(Contrato)

class AditivoInstanceInline(admin.TabularInline):
    model = Aditivo
    extra = 0

class ContratoAdmin(admin.ModelAdmin):
    inlines = [AditivoInstanceInline]


admin.site.register(Contrato, ContratoAdmin)