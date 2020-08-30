from django.contrib import admin
from .models import FormModel, Profile, CsvFile
# Register your models here.

@admin.register(FormModel)
class FormModelAdmin(admin.ModelAdmin):
    list_display = ["user", "first_name","last_name", "Id_number", "dob","gender"]
    search_fields = ['user__username',]


@admin.register(Profile)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ["user","phon_number","email","date","amountD", "amountS","amountB"]
    search_fields = ['user',"phon_number","email"]

@admin.register(CsvFile)
class CsvFileAdmin(admin.ModelAdmin):
    list_display = ["user", "csv_file"]

