from django.urls import path
from . import views

urlpatterns = [
    path("categories/add", views.add_category, name="add_category"),
    path("categories", views.get_categories, name="get_categories"),
    path(
        "categories/<int:category_id>/delete",
        views.delete_category,
        name="delete_category",
    ),
    path(
        "categories/<int:category_id>/update",
        views.update_category,
        name="update_category",
    ),
    path("products/add/", views.add_product, name="add_product"),
    path("products/", views.get_products, name="get_products"),
]
