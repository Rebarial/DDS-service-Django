from django.shortcuts import render, redirect, get_object_or_404
from dds_service.models import Category
from dds_service.forms.categories import CategoryForm

def list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})

def edit(request, pk):
    category_instance = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category_instance)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryForm(instance=category_instance)
    return render(request, 'categories/category_form.html', {'form': form})

def delete(request, pk):
    category_instance = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category_instance.delete()
        return redirect('categories_list')
    return render(request, 'categories/category_confirm_delete.html', {'instance': category_instance})