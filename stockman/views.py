from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import Categories, Products
import json
from django.core import serializers


@require_POST
def add_category(request):
    data = json.loads(request.body)
    name = data["category_name"]

    c = Categories(category_name=name)
    c.save()

    return JsonResponse({"ok": True, "id": c.id}, status=201)


@require_GET
def get_categories(request):
    r = Categories.objects.all()
    r = r.products_set.all()
    data = serializers.serialize("json", r)
    print(type(data))

    return JsonResponse({"ok": True, "data": data})


@require_POST
def delete_category(request, category_id):
    c = Categories.objects.filter(id=category_id)
    print(c)

    if not c:
        return JsonResponse({"ok": False}, status=404)

    c.delete()
    return JsonResponse({"ok": True})


@require_POST
def update_category(request, category_id):
    data = json.loads(request.body)
    name = data["category_name"]

    try:
        c = Categories.objects.get(id=category_id)

        c.category_name = name
        c.save()

        return JsonResponse({"ok": True})
    except Categories.DoesNotExist:
        return JsonResponse({"ok": False}, status=404)


@require_POST
def add_product(request):
    data = json.loads(request.body)

    category_id = data["category_id"]
    product_name = data["product_name"]
    price = data["price"]

    p = Products.objects.create(
        category_id=category_id, product_name=product_name, price=price
    )
    p.save()
    print(p)

    return JsonResponse({"hel": "aa"})


@require_GET
def get_products(request):
    r = Products.objects.all().select_related("category")
    data = serializers.serialize("json", r)
    print(data)

    return JsonResponse({"ok": True, "data": data})
