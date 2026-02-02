from django.contrib import admin


from .models import DataValue, ExcelFiles, Meter
admin.site.register(DataValue)
admin.site.register(Meter)
admin.site.register(ExcelFiles)

