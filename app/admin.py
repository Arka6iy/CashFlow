from django.contrib import admin

from .models import Category, Combo, Kind, Status, SubCategory, Transaction


@admin.register(Transaction)
class CreateAdmin(admin.ModelAdmin):
    list_display = ("created_at", "status", "combo", "amount", "note")


@admin.register(Combo)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("kind", "category", "sub_category")


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
