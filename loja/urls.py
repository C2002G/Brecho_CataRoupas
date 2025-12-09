from django.urls import path
from . import views

app_name = "loja"

urlpatterns = [
    path("", views.LojaView.as_view(), name="index"),
    path("produto/<slug:slug>/", views.produto_detalhe, name="produto_detalhe"),
    # URLs de administração (páginas secretas)
    path("secret-admin-login/", views.admin_login, name="admin_login"),
    path("secret-admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("secret-admin-produto/", views.admin_produto_form, name="admin_produto_add"),
    path(
        "secret-admin-produto/<int:produto_id>/",
        views.admin_produto_form,
        name="admin_produto_edit",
    ),
    path(
        "secret-admin-produto-delete/<int:produto_id>/",
        views.admin_produto_delete,
        name="admin_produto_delete",
    ),
    path(
        "secret-admin-categoria/",
        views.admin_categoria_form,
        name="admin_categoria_add",
    ),
]
