from django.shortcuts import render, redirect, get_object_or_404
from dds_service.models import Subcategory
from dds_service.forms.subcategories import SubcategoryForm

def list(request):
    subcategories = Subcategory.objects.select_related('category').all()
    return render(request, 'subcategories/subcategory_list.html', {'subcategories': subcategories})

def create(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategories_list')
    else:
        form = SubcategoryForm()
    return render(request, 'subcategories/subcategory_form.html', {'form': form})

def edit(request, pk):
    subcategory_instance = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory_instance)
        if form.is_valid():
            form.save()
            return redirect('subcategories_list')
    else:
        form = SubcategoryForm(instance=subcategory_instance)
    return render(request, 'subcategories/subcategory_form.html', {'form': form})

def delete(request, pk):
    subcategory_instance = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        subcategory_instance.delete()
        return redirect('subcategories_list')
    return render(request, 'subcategories/subcategory_confirm_delete.html', {'instance': subcategory_instance})