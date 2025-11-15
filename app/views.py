from django.shortcuts import render, redirect, get_object_or_404
from app.models import ProductModel

# Create your views here.


def index(request):
    products = ProductModel.objects.all().order_by("-created_at")
    context = {
        "products": products,
    }
    return render(request, "index.html", context)


def product_create(request):
    if request.method == "POST":
        product = ProductModel.objects.create(
            name=request.POST.get("name"),
            price=request.POST.get("price"),
        )
        product.save()
        return redirect("/")


def product_update(request, pk):
    if request.method == "POST":
        product = get_object_or_404(ProductModel, id=pk)
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.save()
        return redirect("/")


def product_delete(request, pk):
    product = get_object_or_404(ProductModel, id=pk)
    product.delete()
    return redirect("/")


def page_not_found(request):
    return render(request, "page_not_found.html")
