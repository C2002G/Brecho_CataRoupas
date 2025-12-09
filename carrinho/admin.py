from django.contrib import admin
from .models import CarrinhoItem


@admin.register(CarrinhoItem)
class CarrinhoItemAdmin(admin.ModelAdmin):
    list_display = ["produto", "session_key", "quantidade", "subtotal", "criado_em"]
    list_filter = ["criado_em"]
    readonly_fields = ["subtotal"]
