from .models import Transaction, Status , Type, Category, SubCategory
from django.contrib import admin


@admin.register(Transaction)
class CreateAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'status', 'kind', 'category', 'amount', 'note')

@admin.register(Status)
class StatusRow(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Type)
class TypeRow(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryRow(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SubCategory)
class SubCategoryRow(admin.ModelAdmin):
    list_display = ('sub_category','data' )