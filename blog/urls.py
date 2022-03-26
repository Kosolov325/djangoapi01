from django.urls import path
from .views import viewAlterar, viewPrincipal, viewDetail, viewDelete, viewCreate, viewAlterar

urlpatterns = [
    path("principal/", viewPrincipal, name = "principal"),
    path("postagem/<int:id>/", viewDetail, name = "detalhe"),
    path("deletar/<int:id>/", viewDelete, name = "delete"),
    path("criar-postagem/", viewCreate, name = "criar"),
    path("alterar/<int:id>/", viewAlterar, name = "alterar"),
]
