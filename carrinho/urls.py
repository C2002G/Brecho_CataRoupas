from django.urls import path
from . import views

app_name = "carrinho"

urlpatterns = [
    path("", views.ver_carrinho, name="ver_carrinho"),
    path(
        "adicionar/<int:produto_id>/",
        views.adicionar_carrinho,
        name="adicionar_carrinho",
    ),
    path(
        "atualizar/<int:item_id>/",
        views.atualizar_quantidade,
        name="atualizar_quantidade",
    ),
    path("remover/<int:item_id>/", views.remover_item, name="remover_item"),
    path("finalizar/", views.finalizar_compra, name="finalizar_compra"),
    path("count/", views.carrinho_count, name="carrinho_count"),
]
