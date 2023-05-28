from django.contrib import admin

from cats.models import Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass
