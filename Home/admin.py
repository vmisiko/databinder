from django.contrib import admin
from .models import FormModel, Profile, CsvFile
# Register your models here.

@admin.register(FormModel)
class FormModelAdmin(admin.ModelAdmin):
    list_display = ["user", "first_name","last_name", "Id_number", "dob","gender"]

@admin.register(Profile)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ["user","phon_number","email","date","amountD", "amountS","amountB"]

@admin.register(CsvFile)
class CsvFileAdmin(admin.ModelAdmin):
    list_display = ["user", "csv_file"]